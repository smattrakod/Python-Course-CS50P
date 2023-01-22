from datetime import date
import sys
import inflect

p = inflect.engine()


def main():

    date_of_birth = input("Date of Birth: ").strip()

    year, month, day = check_input(date_of_birth)

    try:
        birth = date(year, month, day)
        today = date.today()
        if birth > today:
            raise ValueError
        days_between = (today - birth)
        min_between = (days_between.days)*24*60
        count = p.number_to_words(min_between, andword="")
        print(count.capitalize(), "minutes")
    except ValueError:
        sys.exit("ValueError")


def check_input(birthdate):
    # Convert from String do date
    try:
        year, month, day = birthdate.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        return year, month, day
    except TypeError:
        sys.exit("Enter Date in Number Format")
    except ValueError:
        sys.exit("Enter you Date of Birth")


if __name__ == "__main__":
    main()
