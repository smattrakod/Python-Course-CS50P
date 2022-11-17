def main():
    user = input("hello how are you doing? ")
    greeting(user)


def greeting(answer):
    answer = answer.lower()
    if answer.startswith("hello"):
        print("$100")
    elif answer.startswith("h"):
        print("$20")
    else:
        print("$0")
    


main()    