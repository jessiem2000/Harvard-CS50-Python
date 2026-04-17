import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if matches := re.findall(r"(\bum\b)",s, re.IGNORECASE):
        umm = len(matches)
        return umm



...


if __name__ == "__main__":
    main()
