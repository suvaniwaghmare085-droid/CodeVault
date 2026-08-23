from datetime import date
from database import load_data, save_data
from utils import safe_float, progress_bar

VALID_DIFFICULTIES = {"Easy", "Medium", "Hard"}


def add_session():
    data = load_data()

    print("\n--- Log Coding Session ---")
    hours = safe_float("Hours coded: ")
    topic = input("Topic studied: ").strip() or "General"
    description = input("What did you work on? ").strip()

    session = {
        "date": str(date.today()),
        "hours": hours,
        "topic": topic,
        "description": description
    }

    data["sessions"].append(session)
    save_data(data)

    print("\n✅ Coding session saved!")


def add_problem():
    data = load_data()

    print("\n--- Add DSA Problem ---")
    name = input("Problem name: ").strip()
    topic = input("Topic: ").strip() or "General"

    difficulty = input("Difficulty (Easy/Medium/Hard): ").strip().capitalize()
    if difficulty not in VALID_DIFFICULTIES:
        print("⚠️  Unrecognized difficulty, defaulting to 'Medium'.")
        difficulty = "Medium"

    problem = {
        "date": str(date.today()),
        "name": name,
        "topic": topic,
        "difficulty": difficulty,
        "status": "Solved"
    }

    data["problems"].append(problem)
    save_data(data)

    print("\n✅ Problem added!")


def view_history(limit=10):
    data = load_data()
    sessions = sorted(data["sessions"], key=lambda s: s["date"], reverse=True)

    print("\n╔══════════════════════════════════════════════╗")
    print("║               CODING HISTORY                  ║")
    print("╠══════════════════════════════════════════════╣")

    if not sessions:
        print("║  No sessions logged yet.                      ║")
    else:
        for s in sessions[:limit]:
            line = f"{s['date']} │ {s['hours']:>4.1f}h │ {s['topic']}"
            print(f"║ {line:<46}║")

    print("╚══════════════════════════════════════════════╝")


def view_dsa_progress():
    data = load_data()
    problems = data["problems"]

    print("\nDSA PROGRESS")
    print("──────────────────────────────")

    if not problems:
        print("No problems logged yet.")
        return

    topics = {}
    for p in problems:
        topics.setdefault(p["topic"], 0)
        topics[p["topic"]] += 1

    max_count = max(topics.values())
    for topic, count in sorted(topics.items(), key=lambda x: -x[1]):
        bar = progress_bar(count, max_count, length=15)
        print(f"{topic:<15} {bar}  ({count})")

    print(f"\nTotal Problems: {len(problems)}")

    difficulties = {"Easy": 0, "Medium": 0, "Hard": 0}
    for p in problems:
        difficulties[p.get("difficulty", "Medium")] = difficulties.get(p.get("difficulty", "Medium"), 0) + 1

    print("\nDifficulty Breakdown")
    for level in ["Easy", "Medium", "Hard"]:
        print(f"  {level:<8}: {difficulties[level]}")


def search_records():
    data = load_data()
    query = input("\nSearch topic/name/description: ").strip().lower()

    if not query:
        print("❌ Empty search — nothing to look for.")
        return

    print(f"\nResults for '{query}':\n")
    found = False

    for s in data["sessions"]:
        haystack = f"{s['topic']} {s.get('description', '')}".lower()
        if query in haystack:
            print(f"[Session] {s['date']} | {s['hours']}h | {s['topic']} — {s.get('description', '')}")
            found = True

    for p in data["problems"]:
        haystack = f"{p['name']} {p['topic']}".lower()
        if query in haystack:
            print(f"[Problem] {p['date']} | {p['name']} ({p['topic']}, {p['difficulty']})")
            found = True

    if not found:
        print("No matching records found.")
