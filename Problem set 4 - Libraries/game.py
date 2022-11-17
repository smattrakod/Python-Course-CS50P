import random


def main():
    guessgame()


def guessgame():
    while True:
        try:
            input_level = int(input("Level: "))
            level = random.randint(1, input_level)
            break
        except ValueError:
            print("", end="")
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                print("", end="")
            elif guess < level:
                print("Too small!")
            elif guess > level:
                print("Too Large!")
            else:
                print("Just right!")
                break
        except ValueError:
            print("", end="")


if __name__ == "__main__":
    main()
