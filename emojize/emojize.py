import emoji

def main():
    rawmoji = (input(("Input: ")))
    remoji = emoji.emojize(f"{rawmoji}", language = 'alias')
    print (remoji)

main()
