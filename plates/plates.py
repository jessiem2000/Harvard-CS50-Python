def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    a =  plate[:2].isalpha()
    b = 2 <= len(plate) <= 6
    c = plate.isalnum()
    d = order(plate)

    valid = [a,b,c,d]

    if all(valid):
        return True
    else:
        return False

def order(plate):
    index = -1
    for i, digit in enumerate(plate):
        if plate.isalpha():
            return True
        elif digit.isdigit():
            index = i
            break
    if index != -1:
        first = plate[:index]
        second = plate[index:]
        if second.startswith("0"):
            return False
        elif second.isdigit():
            return True
    else:
        return False


main()
