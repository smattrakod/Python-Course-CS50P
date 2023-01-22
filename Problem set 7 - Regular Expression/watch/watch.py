import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"^<iframe(?:.*)? src=\"(https?://)(?:www.)?(youtube).com/embed(/.*)></iframe>$", s, re.IGNORECASE):
        group2 = matches.group(2)[:5] + "." + matches.group(2)[5:]
        group3, shit = matches.group(3).split("\"", maxsplit=1)
        new_html = matches.group(1) + group2 + group3
        return new_html


if __name__ == "__main__":
    main()
