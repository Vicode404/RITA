from datetime import datetime
from zoneinfo import ZoneInfo
import random


def show_welcome():
    print("╔══════════════════════════════════╗")
    print("║          RITA v0.1 🤖            ║")
    print("║       Personal Assistant         ║")
    print("╚══════════════════════════════════╝")
    print()


def main():
    show_welcome()

    while True:
        command = input("You > ")

        if command == "quit":
            print("RITA > See you soon 👋")
            break

        elif command == "yo":
            print("RITA > Yo! How are you?")

        elif command == "help":
            print("RITA > Available commands:")
            print("      yo")
            print("      hour")
            print("      date")
            print("      joke")
            print("      quit")

        elif command == "hour":
            current_time = datetime.now(ZoneInfo("Europe/Paris")).strftime("%H:%M")
            print(f"RITA > It is {current_time}.")

        elif command == "date":
            current_date = datetime.now().strftime("%d/%m/%Y")
            print(f"RITA > Today's date is {current_date}.")

        elif command == "joke":
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
                "There are only 2 kinds of people: those who understand binary and those who don't. 🤓",
                "Why was the computer cold? It left its Windows open. 🪟"
            ]

            print("RITA > " + random.choice(jokes))

        else:
            print("RITA > Idk this command yet :( )")


if __name__ == "__main__":
    main()

