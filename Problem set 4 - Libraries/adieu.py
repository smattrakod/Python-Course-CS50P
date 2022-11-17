import inflect

p = inflect.engine()


def main():
    bye()


def bye():
    names = []
    while True:
        try:
            name = input("Name: ").title()
            names.append(name)
        except KeyboardInterrupt:
            break
    names = p.join(names)
    print("Adieu, adieu, to " + names)


if __name__ == "__main__":
    main()
