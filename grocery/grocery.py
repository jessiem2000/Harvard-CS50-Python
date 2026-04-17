def main():
    item_list = []
    item_count = {}
    while True:
        try:
            item = input("").upper().strip()
            item_list.append(item)
        except EOFError:
            break
    for item in item_list:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    for item in item_count:
        if item in item_count:
            count = item_count.get(item)
    for item, count in sorted(item_count.items()):
        print(f"{count} {item}")


main()
