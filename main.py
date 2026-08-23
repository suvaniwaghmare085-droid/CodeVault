from database import create_database
from tracker import add_session, add_problem, view_history, view_dsa_progress, search_records
from insights import show_statistics, summary_counts
from streak import show_streak, calculate_current_streak
from goals import set_daily_goal, show_today_progress
from export import export_report


def print_dashboard():
    counts = summary_counts()
    streak = calculate_current_streak()

    print("\n╔══════════════════════════════════════════════════╗")
    print("║                    CODEVAULT                      ║")
    print("║          Personal Coding Progress Tracker         ║")
    print("╠══════════════════════════════════════════════════╣")
    print(f"║ 🔥 Current Streak     : {streak:<26} ║")
    print(f"║ 💻 Problems Solved    : {counts['problems']:<26} ║")
    print(f"║ ⏱  Total Coding Hours  : {counts['hours']:<25.1f} ║")
    print(f"║ 📚 Topics Covered     : {counts['topics']:<26} ║")
    print("╚══════════════════════════════════════════════════╝")


MENU = """
1. Log Coding Session
2. Add DSA Problem
3. View Coding History
4. View DSA Progress
5. View Statistics
6. View Streak
7. Set Daily Goal
8. Search Records
9. Export Report
0. Exit
"""


def menu():
    while True:
        print_dashboard()
        print(MENU)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_session()
        elif choice == "2":
            add_problem()
        elif choice == "3":
            view_history()
        elif choice == "4":
            view_dsa_progress()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            show_streak()
        elif choice == "7":
            set_daily_goal()
        elif choice == "8":
            search_records()
        elif choice == "9":
            export_report()
        elif choice == "0":
            print("\n👋 Keep coding. Keep growing!")
            break
        else:
            print("\n❌ Invalid choice. Try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    create_database()
    menu()
