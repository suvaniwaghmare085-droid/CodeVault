from datetime import date, timedelta
from database import load_data


def calculate_current_streak():
    """Consecutive days of coding counting back from today (or yesterday)."""
    data = load_data()
    dates = {session["date"] for session in data["sessions"]}

    if not dates:
        return 0

    # Allow streak to still count if today hasn't been logged yet but yesterday was
    current = date.today()
    if str(current) not in dates:
        current -= timedelta(days=1)

    streak = 0
    while str(current) in dates:
        streak += 1
        current -= timedelta(days=1)

    return streak


def calculate_longest_streak():
    """Longest run of consecutive days ever logged."""
    data = load_data()
    dates = sorted({date.fromisoformat(s["date"]) for s in data["sessions"]})

    if not dates:
        return 0

    longest = 1
    current_run = 1

    for i in range(1, len(dates)):
        if dates[i] - dates[i - 1] == timedelta(days=1):
            current_run += 1
            longest = max(longest, current_run)
        elif dates[i] != dates[i - 1]:
            current_run = 1

    return longest


def show_streak():
    current = calculate_current_streak()
    longest = calculate_longest_streak()

    print("\n╔══════════════════════════════════╗")
    print("║           STREAK TRACKER          ║")
    print("╠══════════════════════════════════╣")
    print(f"║ 🔥 Current Streak : {current:>3} days      ║")
    print(f"║ 🏆 Longest Streak : {longest:>3} days      ║")
    print("╚══════════════════════════════════╝")
