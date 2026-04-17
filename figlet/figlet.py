import random
import sys
import pyfiglet

def main():
    from pyfiglet import Figlet
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 3:
        if (sys.argv[1]) in ["-f", "--font"] and (sys.argv[2]) in fonts:
            font = sys.argv[2]
            text = str(input("Input: "))
            text = pyfiglet.figlet_format(f"{text}", font = f"{font}")
            print(text)
        else:
            sys.exit("Invalid Usage")
    elif len(sys.argv) == 1:
        text = str(input("Input: "))
        font = random.choice(fonts)
        text = pyfiglet.figlet_format(f"{text}", font = f"{font}")
        print(text)
    else:
        sys.exit("Invalid Usage")

main()




