from datetime import date, datetime
import inflect
import sys
p = inflect.engine()


def main():
    try:
        birthday = date.fromisoformat((input("Date of Birth: ")))
        today = date.today()
        seasons = today - birthday
        days = seasons.days
        minutes = convert(days)
        print(f'{p.number_to_words(minutes, andword="").capitalize()} minutes')
    except ValueError:
        sys.exit("Invalid Date")

def convert(n):
    minutes = n * 1440
    return minutes



if __name__ == "__main__":
    main()
