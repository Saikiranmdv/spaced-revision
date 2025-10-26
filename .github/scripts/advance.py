import os, json, re
from pathlib import Path
from datetime import datetime, timedelta

TRACKER_FILE = Path("revision_tracker.json")
NOTES_DIR = Path("notes")

STAGE_ORDER = ["notes", "1-day", "3-days", "7-days", "1-week", "1-month", "3-months"]
STAGE_DAYS = {
    "1-day": 1,
    "3-days": 3,
    "7-days": 7,
    "1-week": 14,
    "1-month": 30,
    "3-months": 90
}

RE_DONE = re.compile(r'(^|\s)@done(\s|$)', re.IGNORECASE)

def load_tracker():
    if not os.path.exists(TRACKER_FILE):
        return {}
    try:
        with open(TRACKER_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return {}  # handle empty file safely
            return json.loads(content)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Could not parse revision_tracker.json: {e}")
        return {}

def save_tracker(data):
    TRACKER_FILE.write_text(json.dumps(data, indent=2))

def strip_done_marker(file: Path) -> bool:
    text = file.read_text(encoding="utf-8", errors="ignore")
    if "@done" in text:
        new_text = RE_DONE.sub(" ", text)
        file.write_text(new_text.strip() + "\n", encoding="utf-8")
        return True
    return False

def next_stage(stage):
    if stage not in STAGE_ORDER:
        return "1-day"
    idx = STAGE_ORDER.index(stage)
    return STAGE_ORDER[idx+1] if idx+1 < len(STAGE_ORDER) else None

if __name__ == "__main__":
    tracker = load_tracker()
    today = datetime.today().date()

    # Step 1: Ensure all notes are in tracker
    for f in NOTES_DIR.glob("*"):
        if f.is_file() and f.name not in tracker:
            tracker[f.name] = {
                "study_date": str(today),
                "stage": "notes",
                "next_due": str(today + timedelta(days=1)),  # default first due = tomorrow
                "pending": False,
                "revisions_done": 0
            }
            print(f"Added new note to tracker: {f.name}")

    # Step 2: Check for @done in notes
    for f in NOTES_DIR.glob("*"):
        if f.is_file():
            if strip_done_marker(f):
                info = tracker.get(f.name, {
                    "study_date": str(today),
                    "revisions_done": 0
                })
                curr_stage = info.get("stage", "notes")
                nxt = next_stage(curr_stage)
                if nxt:
                    info["stage"] = nxt
                    info["next_due"] = str(today + timedelta(days=STAGE_DAYS[nxt]))
                    info["pending"] = False
                    info["revisions_done"] += 1
                    tracker[f.name] = info
                    print(f"Advanced {f.name} → {nxt}, next due {info['next_due']}")

    save_tracker(tracker)
    print("Tracker updated.")
