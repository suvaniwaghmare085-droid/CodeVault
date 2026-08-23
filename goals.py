from datetime import date
from database import load_data, save_data
from utils import safe_float, progress_bar


def set_daily_goal():
    data = load_data()

    print("\n--- Set Daily Coding Goal ---")
    goal = safe_float("Daily coding goal (hours): ", default=data["profile"]["daily_goal"])

    data["profile"]["daily_goal"] = goal
    save_data(data)

    print(f"\n✅ Daily goal set to {goal} hours.")


def show_today_progress():
    data = load_data()
    today = str(date.today())
    goal = data["profile"].get("daily_goal", 2)

    hours_today = sum(s["hours"] for s in data["sessions"] if s["date"] == today)

    print("\nTODAY'S PROGRESS\n")
    print(progress_bar(hours_today, goal, length=25))
    print(f"\n{hours_today:.1f} / {goal:.1f} hours")
