def main():
    interpreter()


def interpreter():
    math = (input("What would you like to calculate? "))
    x, y, z = math.split()

    if "." in x:
        x = float(x)
    else:
        x = int(x)  

    if "." in z:
        z = float(z)
    else:
        z = int(z)  

    match y:
        case "+":
            print(x+z)
        case "-":
            print(x-z) 
        case "*":
            print(x*z)
        case "/":
            print(x/z)


main()   