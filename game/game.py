import random
import sys
global level

def main():

    while True:
        try:
            number  = input("Level: ")
            if number.isdigit() and int(number) > 0 :
                numint = int(number)
                a = 1
                r = random.randint(a, numint)
                level = int(r)
                print(level)
                guess(level)
            else:
                pass
        except EOFError:
            sys.exit()

def guess(level):
    while True:
        try:
            guess = input("Guess: ")
            if guess.isdigit() and int(guess) > 0:
                if int(guess) == int(level):
                    print("Just right!")
                    sys.exit()
                elif int(guess) < int(level):
                    print("Too small!")
                elif int(guess) > int(level):
                    print ("Too large!")
            else:
                pass
        except EOFError:
            sys.exit()


main()

