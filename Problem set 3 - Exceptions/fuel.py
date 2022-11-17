def main():
    fuelfraction()

def fuelfraction():
    try:
        x , y = input("Fraction: ").split("/")
        x = float(x)
        y = float(y)
        percent = round((x/y)*100, 2)
    except ValueError:
        print("Write integers")
        fuelfraction()
    except ZeroDivisionError:
        print("No division with 0")
        fuelfraction()
    else:
        if x > y:
            print("impossible fraction")
            fuelfraction()
        else:
            print(f"{percent}%")


if __name__ == "__main__":
    main()