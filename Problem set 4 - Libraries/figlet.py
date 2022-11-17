import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    inp = input("Input: ")
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
    print(figlet.renderText(inp))


elif len(sys.argv) == 3:
    if sys.argv[2] not in figlet.getFonts():
        print("Font doesn't exist")
        sys.exit()

    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        font = figlet.setFont(font=sys.argv[2])
        inp = input("Input: ")
        print(figlet.renderText(inp))

    else:
        sys.exit()


else:
    print("0 eller 2 argument!")
    sys.exit()
