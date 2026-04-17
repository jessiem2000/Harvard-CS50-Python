PRICES = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0.0
    while True:
        try:
            item = input("Item: ").title()
            if item in PRICES.keys():
                total += PRICES[item]
                print(f"Total: ${total:.2f}")

        except KeyError:
            pass
        except EOFError:
            break
    print(f"\nTotal: ${total:.2f}")

main()
