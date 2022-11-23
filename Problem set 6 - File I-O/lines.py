import sys


def main():
    check_sys_error()
    print(f"Number of Lines in this file is: {lines_in_file()}")


def lines_in_file():
    number_of_lines = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.startswith("#") or line.isspace():
                    pass
                else:
                    number_of_lines += 1
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()
    return number_of_lines


def check_sys_error():
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) == 2 and sys.argv[1].endswith(".py") == False:
        print("Not a Python file")
        sys.exit()
    else:
        pass


if __name__ == "__main__":
    main()
