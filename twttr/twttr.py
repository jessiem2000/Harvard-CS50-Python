def main():
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    twitter = (input("Input: "))
    twttr = list(twitter)
    new_list = []
    for letter in twttr:
        if letter in vowels:
            letter = ""
        new_list.append(letter)
    twttrlow = "".join(new_list)
    print(f"Output: {twttrlow}")

main()
