
def main():
    fract = input("Fraction: ")
    percent = convert(fract)
    fuel = gauge(percent)
    print(fuel)

def convert(fract):
    while True:
        try:
            numerator, denominator = fract.split("/")
            if not str(numerator).isdigit() or not str(denominator).isdigit():
                raise ValueError()
            x = int(numerator)
            y = int(denominator)
            if y == 0:
                raise ZeroDivisionError()
            if x > y:
                raise ValueError()
            percent = round(x / y, 2) * 100
            if not 100 >= percent >= 0:
                raise ValueError()

        except EOFError:
            break
        else:
            break
    return percent





def gauge(percent):
    if percent >= 99.0 :
        fuel = "F"
        return fuel
    elif percent <= 1.0 :
        fuel = "E"
        return fuel
    else:
        percent = int(percent)
        fuel = (f"{percent}%")
        return fuel


if __name__ == "__main__":
    main()



