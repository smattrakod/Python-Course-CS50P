import sys


def main():
    fraction = input("Input Fraction (X/Y): ")
    print(gauge(convert(fraction)))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        if y == "0":
            raise ZeroDivisionError
        x = float(x)
        y = float(y)
        percent = int(round((x / y) * 100, 0))
        if percent > 100:
            raise ValueError(print("X <= Y"))
        if percent < 0:
            raise ValueError(print("Negative numbers"))
    except ValueError:
        quit()
    except ZeroDivisionError:
        print("Cant divide with zero")
        quit()
    return percent


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
