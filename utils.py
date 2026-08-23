def safe_float(prompt, default=0.0):
    """Ask for a float and keep re-asking until valid input is given."""
    while True:
        raw = input(prompt).strip()
        if raw == "":
            return default
        try:
            return float(raw)
        except ValueError:
            print("❌ Please enter a valid number.")


def safe_int(prompt, default=0):
    while True:
        raw = input(prompt).strip()
        if raw == "":
            return default
        try:
            return int(raw)
        except ValueError:
            print("❌ Please enter a valid whole number.")


def progress_bar(current, total, length=20):
    """Return a text progress bar like ████████░░░░ 60%"""
    if total <= 0:
        percent = 0
    else:
        percent = min(current / total, 1.0)

    filled = int(length * percent)
    bar = "█" * filled + "░" * (length - filled)
    return f"{bar} {percent * 100:.0f}%"


def print_header(title):
    width = 44
    print("\n╔" + "═" * width + "╗")
    print("║" + title.center(width) + "║")
    print("╠" + "═" * width + "╣")


def print_footer():
    print("╚" + "═" * 44 + "╝")
