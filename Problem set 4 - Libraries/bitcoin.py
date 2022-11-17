import requests
import sys
import json


class Error(Exception):
    pass


class wrongLengthError(Error):
    pass


def main():
    bitcoin_req()


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def cmdLineError():
    try:
        if len(sys.argv) != 2:
            raise wrongLengthError
        if isfloat(sys.argv[1]) == False:
            raise ValueError
        if isfloat(sys.argv[1]) == True and float(sys.argv[1]) < 0:
            raise ValueError
    except ValueError:
        print("You must enter a positive number")
        sys.exit()
    except wrongLengthError:
        print("You must enter ONE Number after the name of the file")
        sys.exit()


def bitcoin_req():
    cmdLineError()
    n_Bitcoins = float(sys.argv[1])
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        # print(json.dumps(r.json(), indent=2))
        o = r.json()
        bitcoin_rate = o["bpi"]["USD"]["rate_float"]
        bitcoin_value = f"{n_Bitcoins * bitcoin_rate:.4f}"
        print(f"{float(bitcoin_value):,}")
    except requests.RequestException:
        print("Request exception, try again")
        sys.exit()


if __name__ == "__main__":
    main()
