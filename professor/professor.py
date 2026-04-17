import random
import sys
global level, answer, count, z
levels = {1: 9, 2: 99, 3: 999}

def main():
    count = 0
    wrong = 0
    score = 10

    while True:
        try:
            level = get_level()

            while count != 10:
                    a = generate_integer(level)
                    b = generate_integer(level)
                    expression = (f"{a} + {b}")
                    answer = eval(expression)
                    while True:
                            z = input(f"{expression} = ").strip()
                            if z.isdigit():
                                z = int(z)
                            try:
                                if answer != z:
                                    wrong += 1
                                    if wrong == 3:
                                        print (f"{expression} = {answer}")
                                        wrong = 0
                                        score -= 1
                                        count += 1
                                        if count == 10:
                                            print(score)
                                            sys.exit()
                                        else:
                                            break
                                    else:
                                        print ("EEE")
                                elif answer == z:
                                    count += 1
                                    wrong = 0
                                    if count == 10:
                                        print(score)
                                        sys.exit()
                                    break
                            except ValueError:
                                print ("EEE")

        except EOFError:
            sys.exit()


def get_level():
    while True:
        try:
            level = input("Level: ")
            if int(level) in levels.keys():
                return level
            else:
                raise ValueError
        except ValueError:
            pass



def generate_integer(level):
    x = 0
    if int(level) == 2:
        x = 10
    elif int(level) == 3:
        x = 100
    y = levels.get(int(level))

    while True:
        try:
            a = random.randint(x, y)
            return a
        except EOFError:
            sys.exit()





if __name__ == "__main__":
    main()


