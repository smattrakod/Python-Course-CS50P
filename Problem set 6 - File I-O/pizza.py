from tabulate import tabulate
import sys


def main():
    check_file_error()
    show_csv()


def check_file_error():
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) == 2 and sys.argv[1].endswith(".csv") == False:
        print("Not a CSV file")
        sys.exit()
    else:
        pass


def show_csv():
    table = []
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                row = line.rstrip().split(",")
                table.append(row)
            print(tabulate(table, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        print("File not found")
        sys.exit()


if __name__ == "__main__":
    main()
