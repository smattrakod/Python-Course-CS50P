from validator_collection import validators, errors


def main():
    print(check_email(input("Enter Email: ")))


def check_email(user_email):
    try:
        email = validators.email(user_email)
        if email:
            return "Valid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
