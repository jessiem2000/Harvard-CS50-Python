import inflect
import sys
p = inflect.engine()
def main():
    name_list = []
    while True:
        try:
            names = input("Name: ")
            name_list.append(names)
            p_list = p.join((name_list), conj = "and")
        except EOFError:
            print('\n'f"Adieu, adieu, to {p_list}")
            sys.exit()

main()
