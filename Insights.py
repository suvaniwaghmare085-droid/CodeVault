from database import load_data


def show_statistics():
    data = load_data()
    sessions = data["sessions"]
    problems = data["problems"]

    total_hours = sum(session["hours"] for session in sessions)
    avg_hours = (total_hours / len(sessions)) if sessions else 0

    topics = {s["topic"] for s in sessions} | {p["topic"] for p in problems}

    print("\n╔══════════════════════════════════════╗")
    print("║              STATISTICS               ║")
    print("╠══════════════════════════════════════╣")
    print(f"║ Coding Sessions   : {len(sessions):>15} ║")
    print(f"║ Problems Solved   : {len(problems):>15} ║")
    print(f"║ Total Coding Hours: {total_hours:>15.1f} ║")
    print(f"║ Avg Hours/Session : {avg_hours:>15.1f} ║")
    print(f"║ Topics Covered    : {len(topics):>15} ║")
    print("╚══════════════════════════════════════╝")


def summary_counts():
    """Small helper used by the dashboard header in main.py"""
    data = load_data()
    total_hours = sum(s["hours"] for s in data["sessions"])
    return {
        "problems": len(data["problems"]),
        "hours": total_hours,
        "topics": len({s["topic"] for s in data["sessions"]} | {p["topic"] for p in data["problems"]})
    }
