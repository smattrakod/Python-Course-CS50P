def main():
    check()

def check():
    file = input("Enter a file name: ")
    file_check = file.casefold()
    filename, suffix = file_check.split(sep=".")
    print(file + " is a", end=": ")
    match suffix:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")  
        case _:
            print("application/octet-stream")          


main()
