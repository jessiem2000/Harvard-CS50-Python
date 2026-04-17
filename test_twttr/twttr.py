vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def main():
    twitter = (input("Input: "))
    twttr = list(twitter)
    twttrlow = shorten(twttr)
    print(f"Output: {twttrlow}")

def shorten(twttr):

    new_list = []
    for letter in twttr:
        if letter in vowels:
            letter = ""
        new_list.append(letter)
    twttrlow = "".join(new_list)
    return twttrlow



if __name__ == "__main__":
    main()
