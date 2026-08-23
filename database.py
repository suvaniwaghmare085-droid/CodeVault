import json
import os

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "codevault.json")

DEFAULT_DATA = {
    "profile": {
        "name": "Developer",
        "daily_goal": 2
    },
    "sessions": [],
    "problems": []
}


def create_database():
    """Create the data folder + JSON file if they don't exist yet."""
    os.makedirs(os.path.dirname(FILE), exist_ok=True)

    if not os.path.exists(FILE):
        with open(FILE, "w") as file:
            json.dump(DEFAULT_DATA, file, indent=4)


def load_data():
    """Load data, always making sure required keys exist (safe for older files)."""
    create_database()

    with open(FILE, "r") as file:
        data = json.load(file)

    # Backfill any missing keys so older save files don't crash the app
    for key, value in DEFAULT_DATA.items():
        if key not in data:
            data[key] = value

    for key, value in DEFAULT_DATA["profile"].items():
        if key not in data["profile"]:
            data["profile"][key] = value

    return data


def save_data(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)
