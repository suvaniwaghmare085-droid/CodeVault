# 🚀 CodeVault

> A personal coding progress tracker built with Python.

CodeVault is a lightweight command-line application that helps developers
track their coding sessions, DSA problems, learning progress, goals, and
coding streaks — all stored locally in a simple JSON file.

```
╔══════════════════════════════════════════════════╗
║                    CODEVAULT                      ║
║          Personal Coding Progress Tracker         ║
╠══════════════════════════════════════════════════╣
║ 🔥 Current Streak     : 2                         ║
║ 💻 Problems Solved    : 1                         ║
║ ⏱  Total Coding Hours  : 4.0                      ║
║ 📚 Topics Covered     : 2                         ║
╚══════════════════════════════════════════════════╝
```

## ✨ Features

- 🔥 Current & longest coding streak tracking
- 💻 DSA problem tracking (with topic + difficulty)
- ⏱ Coding session & hour tracking
- 📚 Topic-based DSA progress dashboard
- 🎯 Daily coding goal with progress bar
- 🔎 Full-text search across sessions and problems
- 📄 Exportable text reports
- 💾 Zero-dependency, JSON-based local storage

## 📁 Project Structure

```
CodeVault/
│
├── main.py          # Entry point + menu loop
├── database.py       # JSON load/save + schema safety
├── tracker.py         # Log sessions, add problems, history, search
├── insights.py        # Statistics dashboard
├── streak.py          # Current & longest streak logic
├── goals.py            # Daily goal setting + progress bar
├── export.py            # Text report generation
├── utils.py              # Shared helpers (progress bars, safe input)
│
├── data/                   # codevault.json lives here (auto-created)
├── reports/                 # Exported reports land here
│
├── README.md
├── requirements.txt
└── .gitignore
```

## ▶️ Run Locally

Requires Python 3.7+. No external packages needed.

```bash
git clone YOUR_REPOSITORY_URL
cd CodeVault
python main.py
```

The `data/codevault.json` file is created automatically on first run.

## 🕹️ Menu Options

```
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
```

## 🛠️ Built With

- Python (standard library only)
- JSON for storage
- File handling & modular design

## 🎯 Future Plans

- Achievement / badge system
- Web dashboard (Flask)
- GitHub API integration for commit analytics
- SQLite backend
- Charts & data visualization

## 📄 License

Free to use, modify, and build on for your own portfolio.
