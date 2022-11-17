from lib2to3.pytree import convert


def main():
    checkmeal = convert(input("what time is it? "))
    if 18 <= checkmeal <= 19:
        print("Dinner time!")
    elif 12 <= checkmeal <= 13:
        print("Lunch time!")
    elif 7 <= checkmeal <= 8:
        print("Breakfast time! ")
        

def convert(time):
    hour, minutes = time.split(":")
    return int(hour) + float(minutes)/60  


main()
