import re
import sys


def main():
    print(convert(input("Hours: ")))
    exit(0)


def convert(s):
    try:
        m = re.search(
            r"^(1?[0-9](:[0-5][0-9])?)( AM| PM) to (1?[0-9](:[0-5][0-9])?)( AM| PM)$", s)
        if m:

            # Start time
            if ":" in m.group(1):
                hour1, min1 = m.group(1).split(":")
                hour1 = int(hour1)
                min1 = int(min1)
                if hour1 > 12:
                    raise ValueError
                if hour1 == 12 and min1 > 59:
                    raise ValueError
                if hour1 == 12:
                    hour1 = 0
            else:
                hour1 = int(m.group(1))
                if hour1 > 12:
                    raise ValueError
                if hour1 == 12:
                    hour1 = 0
            # End time
            if ":" in m.group(4):
                hour2, min2 = m.group(4).split(":")
                hour2 = int(hour2)
                min2 = int(min2)
                if hour2 > 12:
                    raise ValueError
                if hour2 == 12 and min2 > 59:
                    raise ValueError
                if hour2 == 12:
                    hour2 = 0
            else:
                hour2 = int(m.group(4))
                if hour2 > 12:
                    raise ValueError
                if hour2 == 12:
                    hour2 = 0
            if m.group(3) == " PM" and hour1 != 12:
                hour1 += 12
            if m.group(6) == " PM" and hour2 != 12:
                hour2 += 12
            if ":" in m.group(1) and ":" in m.group(4):
                return f"{hour1:02}:{min1:02} to {hour2:02}:{min2:02}"
            elif ":" in m.group(1) and ":" not in m.group(4):
                return f"{hour1:02}:{min1:02} to {hour2:02}:00"
            elif ":" not in m.group(1) and ":" in m.group(4):
                return f"{hour1:02}:00 to {hour2:02}:{min2:02}"
            else:
                return f"{hour1:02}:00 to {hour2:02}:00"

        else:
            raise ValueError
    except ValueError:
        sys.exit("ValueError")


if __name__ == "__main__":
    main()
