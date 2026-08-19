from datetime import datetime
from zoneinfo import ZoneInfo
import random


def show_welcome():
    print("╔══════════════════════════════════╗")
    print("║          RITA v0.1 🤖            ║")
    print("║       Personal Assistant         ║")
    print("╚══════════════════════════════════╝")
    print()


def show_help():
    print("RITA > Available commands:")
    print("      yo   - Say hello")
    print("      hour - Show the current time")
    print("      date - Show today's date")
    print("      joke - Tell a random joke")
    print("      help - Show available commands")
    print("      quit - Exit RITA")


def get_time():
    current_time = datetime.now(
        ZoneInfo("Europe/Paris")
    ).strftime("%H:%M")

    print(f"RITA > It is {current_time}.")


def get_date():
    current_date = datetime.now(
        ZoneInfo("Europe/Paris")
    ).strftime("%d/%m/%Y")

    print(f"RITA > Today's date is {current_date}.")


def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "There are only 10 kinds of people: those who understand binary and those who don't. 🤓",
        "Why was the computer cold? It left its Windows open. 🪟"
    ]

    print("RITA > " + random.choice(jokes))


def main():
    show_welcome()

    while True:
        command = input("You > ").lower().strip()

        if command == "quit":
            print("RITA > See you soon 👋")
            break

        elif command == "yo":
            print("RITA > Yo!  👋")

        elif command == "help":
            show_help()

        elif command == "hour":
            get_time()

        elif command == "date":
            get_date()

        elif command == "joke":
            tell_joke()

        else:
            print("RITA > Idk this command yet :(")


if __name__ == "__main__":
    main()