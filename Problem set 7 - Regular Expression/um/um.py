import re


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    mnt = re.findall(r"\bum\b", s)
    return len(mnt)


if __name__ == "__main__":
    main()
