import datetime

def main():
    change_date()

def change_date():
# Changes dates from "Month day, year" Where month is Text to YYYY-MM-DD
# Or from MM/DD/YYYY to YYYY-MM-DD
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    m = "asdf"
    month_nr = 0
    date = input("Date: ")
    for month in months:
        if month in date:
            m = month
            month_nr = months.index(month) + 1
    if m in months:
        try:
            m, d, y = date.split(" ")
            d = int(d.rstrip(","))
            y = int(y)
            s = datetime.date(y,month_nr,d)
            print(f"{y}-{month_nr:02}-{d:02}")
        except ValueError:
            print("Invalid Date or Format")
            change_date()
    else: 
        try:
            m, d, y = map(int,date.split("/"))
            s = datetime.date(y,m,d)
            print(f"{y}-{m:02}-{d:02}")
        except ValueError:
            print("Invalid Date or Format")
            change_date()




if __name__ == "__main__":
    main()