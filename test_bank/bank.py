def main():
    greeting = input("Greeting:")
    dollar = value(greeting)
    print(f"${dollar}")




def value(greeting):
    greeting = (greeting).strip().lower()
    if greeting.startswith(("hello")):
        return(0)
    elif greeting.startswith(("h", "H")):
        return(20)
    else:
        return(100)

if __name__ == "__main__":
    main()
