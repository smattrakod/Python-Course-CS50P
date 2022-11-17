def main():
    user_answer = input("what is the answer to the Great Question of Life, the Universe and Everything? ")
    deep_thought(user_answer)

def deep_thought(input):
    match input:
        case "42" | "forty two" | "Forty two" | "forty-two" | "Forty-two":
            print("Yes!")
        case _:
            print("No!")

main()