import sys
global argfile, arg


def main():
    lengthcount = 0
    argfile = sys.argv[1]
    arg = sys.argv

    file_check(arg)
    try:
        with open(argfile, "r") as f:
            for line in f:
                if not line.strip():
                    lengthcount += 1
                if line.strip().startswith("#"):
                    lengthcount += 1
        with open(argfile) as f:
            linecount = f.readlines()
            lineamount = (len(linecount))
            print(lineamount - lengthcount )
    except FileNotFoundError:
        sys.exit("File does not exist")


def file_check(arg):
    try:
        ext = arg[1].lower().strip().split(".")
        extension = ext[1:2]
        if len(arg) > 2:
            sys.exit("Too many command-line arguments")
        elif len(arg) < 2:
            sys.exit("Too few command-line arguments")
        elif extension != ['py']:
            sys.exit("Not a Python file")
    except FileNotFoundError:
        sys.exit("File does not exist")

main()
