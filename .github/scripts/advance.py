import os
import re
import shutil
from pathlib import Path

# Stage order (left -> right). Anything in 'notes/' goes to '1-day' first.
STAGES = ["notes", "1-day", "3-days", "7-days", "1-week", "1-month", "3-months"]

RE_DONE = re.compile(r'(^|\s)@done(\s|$)', re.IGNORECASE)

REPO_ROOT = Path(__file__).resolve().parents[2]  # repo root from .github/scripts
STAGE_DIRS = [REPO_ROOT / s for s in STAGES]

def ensure_dirs():
    for d in STAGE_DIRS:
        d.mkdir(parents=True, exist_ok=True)

def is_marked_done_by_name(p: Path) -> bool:
    # e.g. notes like "topic.done.md" or "topic.done"
    stem = p.stem  # filename without suffix
    return stem.endswith(".done")

def strip_done_from_name(p: Path) -> Path:
    # Turn "file.done.md" -> "file.md" ; "file.done" -> "file"
    if p.stem.endswith(".done"):
        new_stem = p.stem[:-5]  # remove ".done"
        return p.with_name(new_stem + p.suffix)
    return p

def is_marked_done_in_content(p: Path) -> bool:
    try:
        # Only check text-like files; skip binaries > 2 MB for safety
        if p.stat().st_size > 2 * 1024 * 1024:
            return False
        text = p.read_text(encoding="utf-8", errors="ignore")
        return RE_DONE.search(text) is not None
    except Exception:
        return False

def remove_done_marker(p: Path):
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
        new_text = RE_DONE.sub(" ", text)
        if new_text != text:
            p.write_text(new_text, encoding="utf-8")
    except Exception:
        # If anything goes wrong, leave file as-is (name-based marker may still handle it)
        pass

def next_stage_dir(current_dir: Path) -> Path | None:
    try:
        idx = STAGE_DIRS.index(current_dir)
    except ValueError:
        return None
    if idx >= len(STAGE_DIRS) - 1:
        return None
    return STAGE_DIRS[idx + 1]

def advance_once():
    moved = []
    for i, stage_dir in enumerate(STAGE_DIRS[:-1]):  # skip last stage
        for p in stage_dir.iterdir():
            if p.is_dir():
                continue
            try:
                mark_by_name = is_marked_done_by_name(p)
                mark_by_content = is_marked_done_in_content(p)
                if not (mark_by_name or mark_by_content):
                    continue

                # Prepare destination path and clean up markers
                dest_dir = next_stage_dir(stage_dir)
                if dest_dir is None:
                    continue

                new_name_path = strip_done_from_name(p)
                if mark_by_content:
                    remove_done_marker(p)

                # If we changed the name, rename before move to keep history sane
                src_path = p
                if new_name_path.name != p.name:
                    src_path = p.with_name(new_name_path.name)
                    p.rename(src_path)

                dest_path = dest_dir / src_path.name
                dest_dir.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src_path), str(dest_path))

                moved.append((stage_dir.name, dest_dir.name, dest_path.name))
            except Exception as e:
                print(f"[warn] Could not process {p}: {e}")
    return moved

if __name__ == "__main__":
    ensure_dirs()
    moves = advance_once()
    if moves:
        print("Advanced files:")
        for a, b, name in moves:
            print(f" - {name}: {a} -> {b}")
    else:
        print("No files marked @done. Nothing to advance.")
