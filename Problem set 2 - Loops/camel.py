
from dataclasses import replace


def main():
    snake_case()


def snake_case():
    name = input("Enter name here: ")
    for letter in name:
        if letter.isupper():
            print(letter.replace(letter , "_" + letter.lower()), end="")
        else:
            print(letter, end="")

if __name__ == "__main__":
    main()




