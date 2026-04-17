import csv
import sys
from tabulate import tabulate

def main():
    arg = sys.argv
    filename = sys.argv[1]
    file_check(arg, filename)
    try:
         with open(filename, newline = '') as f:
            reader = csv.reader(f)
            Dreader = csv.DictReader(f)
            print(tabulate(reader, headers=Dreader.fieldnames, tablefmt="grid"))




    except FileNotFoundError:
         sys.exit("File does not exist")


def file_check(arg, filename):
    if len(arg) > 2:
            sys.exit("Too many command-line arguments")
    elif len(arg) < 2:
            sys.exit("Too few command-line arguments")
    else:
        if filename.endswith(".csv"):
            pass
        else:
            sys.exit("Not a CSV file")




main()
