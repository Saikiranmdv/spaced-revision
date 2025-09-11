import os
from pathlib import Path
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    raise SystemExit("Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID env vars")

STAGES = ["notes", "1-day", "3-days", "7-days", "1-week", "1-month", "3-months"]
REPO_ROOT = Path(__file__).resolve().parents[2]

def list_stage(folder: str):
    p = (REPO_ROOT / folder)
    if not p.exists():
        return []
    return sorted([f.name for f in p.iterdir() if f.is_file()])

def send(msg: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    r = requests.post(url, data=payload, timeout=20)
    r.raise_for_status()

if __name__ == "__main__":
    lines = ["📚 Today's Study Revision"]
    has_any = False
    for stage in STAGES:
        files = list_stage(stage)
        if files:
            has_any = True
            lines.append(f"\n📂 {stage}:")
            lines.extend(f"- {name}" for name in files)

    if not has_any:
        lines = ["✅ No scheduled study items today!"]

    send("\n".join(lines))
