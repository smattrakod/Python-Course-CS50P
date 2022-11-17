def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()
    notOK = [".", ",", "!", "?", "-", "_", " "]
    i = 0
    nr = 0
    if len(s) < 2 or len(s) > 6:
        print("Wrong length")
        return False
    else:
        for char in s:
            if char.isnumeric():
                if char == "0" and nr == 0:
                    print("0 cant be first number!")
                    return False
                nr += 1
            if char.isnumeric() == False and nr > 0:
                print("only numbers in the end")
                return False
            if char.isnumeric() and i < 2:
                print("No numbers in the first 2 spots!")
                return False
            for sign in notOK:
                if char == sign:
                    print("Only letters and numbers!")
                    return False
            i += 1
        print("Plate " + s + " is ", end="")
        return True




if __name__ == "__main__":
    main()