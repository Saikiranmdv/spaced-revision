import os, json
from datetime import datetime
import requests

TRACKER_FILE = "revision_tracker.json"

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send(msg: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    r = requests.post(url, data={"chat_id": CHAT_ID, "text": msg}, timeout=20)
    r.raise_for_status()

if __name__ == "__main__":
    if not os.path.exists(TRACKER_FILE):
        send("📚 No revision data found yet.")
        exit()

    tracker = json.load(open(TRACKER_FILE))
    today = datetime.today().date()

    due_today, pending = [], []

    for fname, info in tracker.items():
        next_due = datetime.fromisoformat(info["next_due"]).date()
        if next_due == today:
            due_today.append(f"{fname} ({info['stage']})")
        elif next_due < today:
            if not info.get("pending", False):
                info["pending"] = True
            pending.append(f"{fname} (was due {next_due}, stage {info['stage']})")

    # save updated tracker (with pending flags)
    json.dump(tracker, open(TRACKER_FILE, "w"), indent=2)

    msg = f"📚 Revision Status for {today}\n\n"
    if due_today:
        msg += "✅ Due Today:\n" + "\n".join(f"- {f}" for f in due_today) + "\n\n"
    if pending:
        msg += "⚠️ Pending:\n" + "\n".join(f"- {f}" for f in pending) + "\n\n"
    if not (due_today or pending):
        msg += "🎉 Nothing due today!"

    send(msg)
    print("Notification sent.")
