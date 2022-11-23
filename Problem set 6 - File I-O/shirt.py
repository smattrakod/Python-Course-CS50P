from PIL import Image
from PIL import ImageOps
import sys


def main():
    check_input()
    fit_images()

# if the user does not specify exactly two command-line arguments,
# if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
# if the input’s name does not have the same extension as the output’s name, or
# if the specified input does not exist.


def check_input():
    if len(sys.argv) != 3:
        print("Input 2 command-lina args")
        sys.exit()
    suffix = [".jpg", ".jpeg", ".png"]
    if sys.argv[1][-4:] not in suffix:
        print("need to end in .jpg, .jpeg, or .png")
        sys.exit()
    if sys.argv[1][-4:] != sys.argv[2][-4:]:
        print("need to be same output file as input file")
        sys.exit()


def fit_images():
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        print("shirt-picture not in folder")
        sys.exit()
    try:
        image_to_fit = Image.open(sys.argv[1])
        image_to_fit = ImageOps.fit(image_to_fit, size=(
            shirt.width, shirt.height))
    except FileNotFoundError:
        print("File Not Found in Folder")
        sys.exit()
    image_to_fit.paste(shirt, shirt)
    image_to_fit.save(sys.argv[2])


if __name__ == "__main__":
    main()
