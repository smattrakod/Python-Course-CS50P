def main():
    print(energy())



def energy():
    c = 300000000
    weight = int(input("Enter mass in kilograms here: "))
    joule = weight * (c ** 2)
    return joule    


main()