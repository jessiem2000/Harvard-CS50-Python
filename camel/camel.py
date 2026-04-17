def main():
    snake_convert = (input("camelCase: "))
    snakecase = list(snake_convert)
    new_list = []
    for character in snakecase:
        if character.isupper():
            character = "_" + character.lower()
        new_list.append(character)
    snaked = "".join(new_list)
    print(f"snake_case: {snaked}")

main()
