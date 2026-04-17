import sys
from PIL import Image, ImageOps

import os


def main():
    arg = sys.argv
    file_check(arg)
    try:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        shirt = Image.open("shirt.png")
        shirt = shirt.convert("RGBA")
        size = shirt.size
        f1 = Image.open(file1)
        f1c = ImageOps.fit(f1, size)
        f1c.paste(shirt, shirt)
        f1c.save(file2)

    except FileNotFoundError:
         sys.exit("Input does not exist")


def file_check(arg):
    valid_ext = [".jpg", ".jpeg", ".png"]
    ext1 = os.path.splitext(arg[1])[1].lower()
    ext2 = os.path.splitext(arg[2])[1].lower()
    if len(arg) > 3:
            sys.exit("Too many command-line arguments")
    elif len(arg) < 3:
            sys.exit("Too few command-line arguments")
    else:
        if ext1 and ext2 in valid_ext:
             if ext1 == ext2:
                pass
             else:
                  sys.exit("Input and Output have different extensions")
        else:
            sys.exit("Invalid Input")


main()
