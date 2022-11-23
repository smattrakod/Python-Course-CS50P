import csv
import sys


def main():
    check_file_error()
    writefile(readfile())


def readfile():
    students = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                students.append(
                    {"first": first, "last": last, "house": row["house"]})
            return students
    except FileNotFoundError:
        print("File Not Found")
        sys.exit()


def writefile(csv_file):
    if sys.argv[2].endswith(".csv") == False:
        print("Need to write to an csv-file")
        sys.exit()
    with open(sys.argv[2], "a") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in csv_file:
            writer.writerow(row)


def check_file_error():
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit()
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) == 3 and sys.argv[1].endswith(".csv") == False:
        print("Need to read a CSV file")
        sys.exit()
    else:
        pass


if __name__ == "__main__":
    main()
