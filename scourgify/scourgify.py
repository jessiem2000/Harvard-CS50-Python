import csv
import sys




def main():
    arg = sys.argv
    filename = sys.argv[1]
    output = sys.argv[2]
    list = file_check(arg, filename)
    slist = []
    for row in list:
        last, first = row["name"].strip().split(",")
        home = row["house"]
        slist.append({"first": first.strip(), "last": last, "house": home})
    with open(output, "w") as fout:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(slist)











def file_check(arg, filename):
    if len(arg) > 3:
            sys.exit("Too many command-line arguments")
    elif len(arg) < 3:
            sys.exit("Too few command-line arguments")
    else:
        list = []
        try:
         with open(filename, newline = '') as f:
            reader = csv.DictReader(f)
            for row in reader:
                list.append(row)
            return list
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[2]}")

main()
