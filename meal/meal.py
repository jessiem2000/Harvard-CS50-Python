def main():
    global minutes, time, hours, current_time
    time = input("What time is it?")
    if time.endswith("a.m."):
        twelveam()
    elif time.endswith("p.m."):
        twelvepm()
    else:
        convert(time)
        if 7.0 <= current_time <= 8.0:
            print("breakfast time")
        elif 12.0 <= current_time <= 13.0:
             print("lunch time")
        elif 18.0 <= current_time <= 19.0:
            print("dinner time")
        else:
            print("")
def convert(time):
    global converted_minutes, current_time, hours
    hours, minutes = time.split(":")
    converted_minutes = ((int(minutes)) / 60)
    current_time = float((sum((float(hours), converted_minutes))))
    return current_time

def convert(twelvetime):
    global converted_minutes, current_time, hours
    hours, minutes = twelvetime.split(":")
    converted_minutes = ((int(minutes)) / 60)
    current_time = float((sum((float(hours), converted_minutes))))
    return current_time

def twelveam():
    global minutes, time, hours, twelvetime
    twelvetime = time.replace("a.m.", "").strip()
    convert(twelvetime)
    if 7.0 <= current_time <= 8.0:
        print("breakfast time")
    else:
        print("")
def twelvepm():
    global minutes, time, hours, twelvetime
    twelvetime = time.replace("p.m.", "").strip()
    convert(twelvetime)
    if 12.0 <= current_time <= 12.99 or current_time == 1.0:
        print("lunch time")
    elif 6.0 <= current_time <= 7.0:
        print("dinner time")
    else:
        print()

if __name__ == "__main__":
    main()
