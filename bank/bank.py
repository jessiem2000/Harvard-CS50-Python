Greeting = (input("Greeting:").strip().lower())

if Greeting.startswith(("hello")):
    print("$0")
elif Greeting.startswith(("h", "H")):
    print("$20")
else: print("$100$")


