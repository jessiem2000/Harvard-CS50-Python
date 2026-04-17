import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    if matches := re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/(.+)\"></iframe>", s):
        domain = matches.group(2)
        url = f"https://youtu.be/{domain}"
        return url
    else:
        return None


if __name__ == "__main__":
    main()
