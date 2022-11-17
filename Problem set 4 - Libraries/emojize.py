import emoji


def main():
    make_emoji()


def make_emoji():
    print("Output: " + emoji.emojize(input("Input: "), language="alias"))


if __name__ == "__main__":
    main()
