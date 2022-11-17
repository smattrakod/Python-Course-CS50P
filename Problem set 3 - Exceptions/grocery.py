def main():
    grocerylist()


def grocerylist():
    x = {}
    while True:
        try:
            item = input("Item: ")
            if item in x:
                x[item] += 1
            else:
                x[item] = 1
        except KeyboardInterrupt:
            print("\n")
            break
    for key in sorted(x):
        print(x[key], key)
        



if __name__ == "__main__":
    main()