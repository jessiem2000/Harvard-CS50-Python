Answer = (input("What is the Answer to the Great Question of Life, The Universe, and Everything?\n").strip().lower())

match Answer:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")
