def main():
    user = input("hello how are you doing? ")
    print(greeting(user))


def greeting(answer):
    answer = answer.lower()
    if answer.startswith("hello"):
        return "$0"
    elif answer.startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
