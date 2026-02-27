#!/usr/bin/env python3

"""
A simple script to display plant information in the Community Garden.
"""


def main() -> None:
    """ Making a plant with a name, height and age (in days) """
    name: str = "Tulip"
    height: int = 25
    age: int = 2

    print("~ Community Garden Plant Information Board ~\n")
    print(f"Plant name: {name}")
    print(f"Plant height: {height} cm")
    print(f"Plant age: {age} days")
    print("~ End of List ~\n")


if __name__ == "__main__":
    main()
