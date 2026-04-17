import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(0?[1-9]|1[0-2])(?::([0-5][0-9]))?\s?(AM|PM) to (0?[1-9]|1[0-2])(?::([0-5][0-9]))?\s?(AM|PM)$", s):
        ftime = [matches.group(1,2,3)]
        ttime = [matches.group(4,5,6)]
        ftime24 = convert24(ftime)
        ttime24 = convert24(ttime)
        return f"{ftime24} to {ttime24}"
    else:
        raise ValueError




def convert24(n):
    pm = {
        "01" : "13",
        "02" : "14",
        "03" : "15",
        "04" : "16",
        "05" : "17",
        "06" : "18",
        "07" : "19",
        "08" : "20",
        "09" : "21",
        "10" : "22",
        "11" : "23",
        "12" : "24",
    }
    for x, y, z in n:
        if y is None:
            y = "00"
        hourf = ""
        if x == "12" and y == "AM":
            x = "00"
        elif z == "PM":
            if len(x) == 1:
                hourf = "0" + x
                x = pm.get(hourf)
            else:
                hourf = x
                x = pm.get(hourf)
    return (f"{int(x):02}:{y}")


if __name__ == "__main__":
    main()
