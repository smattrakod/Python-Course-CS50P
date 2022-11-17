def main():
    shorten()


def letter_check(letter):
    vocals = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for vocal in vocals:
        if letter == vocal:
            return True


def shorten():
    s = input("Input: ")
    for letter in s:
        if letter_check(letter):
            print("", end="")
        else:
            print(letter, end="")


if __name__ == "__main__":
    main()
