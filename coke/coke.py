def main():
    while True:
        coins = [5, 10, 25]
        print("Amount Due: 50")
        total = 50
        due = int(input("Insert coin: "))
        if due in coins:
            change = remaining(total, due)
            while True:
                if change > 0:
                    print(f"Amount Due: {change}")
                    total = change
                    due = int(input("Insert Coin: "))
                    change = remaining(total, due)
                if change <= 0:
                    print(f"Change Owed: {abs(change)}")
                    break
            break

def remaining(total,due):
    return total - due

main()

