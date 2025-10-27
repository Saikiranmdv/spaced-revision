import json, datetime, re
from pathlib import Path

tracker = json.load(open("revision_tracker.json"))
today = datetime.date.today()

# --- build dashboard content ---
lines = [f"## 📊 Dashboard (auto-updated daily)\n",
         f"_Last updated: {today}_\n"]

# Stage distribution
stages = {}
for _, info in tracker.items():
    stages[info["stage"]] = stages.get(info["stage"], 0) + 1
lines.append("\n### Stage Distribution")
for stage, count in stages.items():
    lines.append(f"- {stage}: {count}")

# Due today
lines.append("\n### ✅ Due Today")
due_today = [f"- [{fname}](notes/{fname}) (stage: {info['stage']})"
             for fname, info in tracker.items()
             if info["next_due"] == str(today)]
if due_today:
    lines.extend(due_today)
else:
    lines.append("- None 🎉")

# Pending
lines.append("\n### ⚠️ Pending")
pending = [f"- [{fname}](notes/{fname}) (was due {info['next_due']}, stage {info['stage']})"
           for fname, info in tracker.items() if info.get("pending", False)]
if pending:
    lines.extend(pending)
else:
    lines.append("- None 🎉")

new_section = "\n".join(lines)

# --- replace in README ---
readme = Path("README.md").read_text()
pattern = re.compile(r"## 📊 Dashboard.*", re.DOTALL)
if pattern.search(readme):
    readme = pattern.sub(new_section, readme)
else:
    readme += "\n\n" + new_section

Path("README.md").write_text(readme)
print("README updated with dashboard.")
