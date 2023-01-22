import re


def main():
    if validate(input("IPv4 Address: ").strip()) == True:
        print("valid")
    else:
        print("invalid")


def validate(ip):
    ipv4 = ip.split(".")
    if len(ipv4) != 4:
        return False
    for number in ipv4:
        if len(number) > 3:
            return False
        if number.isnumeric() == False:
            return False
        elif len(number) < 3 and re.search(r"^[0-9]?[0-9]?$", number):
            pass
        elif len(number) == 3 and re.search(r"^[0-2]?[0-5]?[0-9]?$", number) and number[0] == "2":
            if int(number[1]) == 5 and int(number[2]) > 5:
                return False
            else:
                pass

        elif len(number) == 3 and re.search(r"^[0-1]?[0-9]?[0-9]?$", number) and number[0] == "1":
            pass
        else:
            return False
    return True


if __name__ == "__main__":
    main()
