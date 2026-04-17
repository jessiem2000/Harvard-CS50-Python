def main():
    percent = frac()
    if percent >= .99 :
        print("F")
    elif percent <= .01 :
        print("E")
    else:
        gauge = (f"{percent:.0%}")
        print(gauge)

def frac():
    while True:
        try:
            fract = input("Fraction: ")
            numerator, denominator = fract.split("/")
            x = int(numerator)
            y = int(denominator)
            percent = (x / y)
            if not 1 >= percent >= 0:
                raise   ValueError()
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            break
    return percent
main()



