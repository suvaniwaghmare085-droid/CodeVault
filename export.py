import os
from datetime import date
from database import load_data
from streak import calculate_current_streak, calculate_longest_streak

REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")


def export_report():
    data = load_data()
    os.makedirs(REPORTS_DIR, exist_ok=True)

    total_hours = sum(s["hours"] for s in data["sessions"])
    filename = f"report_{date.today()}.txt"
    filepath = os.path.join(REPORTS_DIR, filename)

    with open(filepath, "w") as f:
        f.write("CODEVAULT REPORT\n")
        f.write(f"Generated: {date.today()}\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Current Streak : {calculate_current_streak()} days\n")
        f.write(f"Longest Streak : {calculate_longest_streak()} days\n")
        f.write(f"Total Sessions : {len(data['sessions'])}\n")
        f.write(f"Total Hours    : {total_hours:.1f}\n")
        f.write(f"Problems Solved: {len(data['problems'])}\n\n")

        f.write("SESSION LOG\n")
        f.write("-" * 40 + "\n")
        for s in sorted(data["sessions"], key=lambda x: x["date"]):
            f.write(f"{s['date']} | {s['hours']}h | {s['topic']} | {s.get('description', '')}\n")

        f.write("\nPROBLEM LOG\n")
        f.write("-" * 40 + "\n")
        for p in sorted(data["problems"], key=lambda x: x["date"]):
            f.write(f"{p['date']} | {p['name']} | {p['topic']} | {p['difficulty']}\n")

    print(f"\n✅ Report exported to reports/{filename}")
