def main():
    input_word = input("Input: ")
    print(shorten(input_word))


def shorten(word):
    vocals = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    short = []
    for letter in word:
        if letter in vocals and letter.isupper():
            print("", end="")
        else:
            short.append(letter)
    short = "".join(short)
    return short


if __name__ == "__main__":
    main()
