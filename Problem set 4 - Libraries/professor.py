import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n < 1 or n > 3:
                raise ValueError
            return n
        except ValueError:
            print("", end="")


def generate_integer(level):
    i = 0
    result = 0
    match level:
        case 1:
            while i < 10:
                X = random.randint(0, 9)
                Y = random.randint(0, 9)
                print(f"{X} + {Y} = ", end="")
                tries = 0
                while True:
                    try:
                        answer = int(input())
                        if answer == (X + Y):
                            result += 1
                            break
                        elif answer != (X + Y):
                            raise ValueError
                    except ValueError:
                        tries = tries + 1
                        if tries == 3:
                            print(f"{X} + {Y} = {X+Y}")
                            break
                        print("EEE")
                        print(f"{X} + {Y} = ", end="")
                i += 1
            print(f"Result = {result}")
        case 2:
            while i < 9:
                X = random.randint(10, 99)
                Y = random.randint(10, 99)
                print(f"{X} + {Y} = ", end="")
                tries = 0
                while True:
                    try:
                        answer = int(input())
                        if answer == (X + Y):
                            result += 1
                            break
                        elif answer != (X + Y):
                            raise ValueError
                    except ValueError:
                        tries = tries + 1
                        if tries == 3:
                            print(f"{X} + {Y} = {X+Y}")
                            break
                        print("EEE")
                        print(f"{X} + {Y} = ", end="")
                i += 1
            print(f"Result = {result}")
        case 3:
            while i < 10:
                X = random.randint(100, 999)
                Y = random.randint(100, 999)
                print(f"{X} + {Y} = ", end="")
                tries = 0
                while True:
                    try:
                        answer = int(input())
                        if answer == (X + Y):
                            result += 1
                            break
                        elif answer != (X + Y):
                            raise ValueError
                    except ValueError:
                        tries = tries + 1
                        if tries == 3:
                            print(f"{X} + {Y} = {X+Y}")
                            break
                        print("EEE")
                        print(f"{X} + {Y} = ", end="")
                i += 1
            print(f"Result = {result}")


if __name__ == "__main__":
    main()
