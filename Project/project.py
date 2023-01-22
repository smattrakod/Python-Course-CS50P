"""Once you have solved each of the course’s problem sets, it’s time to implement your final project, a Python program of your very own! The design and implementation of your project is entirely up to you, albeit subject to these requirements:

Your project must be implemented in Python.
Your project must have a main function and three or more additional functions. At least three of those additional functions must be accompanied by tests that can be executed with pytest.
Your main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of your project.
Your 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under any classes or functions).
Your test functions must be in a file called test_project.py, which should also be in the “root” of your project. Be sure they have the same name as your custom functions, prepended with test_ (test_custom_function, for example, where custom_function is a function you’ve implemented in project.py).
You are welcome to implement additional classes and functions as you see fit beyond the minimum requirement.
Implementing your project should entail more time and effort than is required by each of the course’s problem sets.
Any pip-installable libraries that your project requires must be listed, one per line, in a file called requirements.txt in the root of your project."""


# Financial statement calculator.
# pip install csv, sys & collections.
# Take a CSV-file which has product, productcategory, revenue, price, date
import csv
import os
import sys
from datetime import date
from collections import Counter


def main():
    sales = readcsv(input("Name of CSV file: "))
    while True:
        print("-------------------------  MENU  --------------------------")
        print("          Most Sold Products Sorted Descending: (Enter: 1) ")
        print("           Products Who Generated Most Revenue: (Enter: 2) ")
        print("                 Total Revenue from the Peroid: (Enter: 3) ")
        print("            Average Revenue per Day/Week/Month: (Enter: 4) ")
        print("   Most Sold Product-Category sorted Desending: (Enter: 5) ")
        print("               Items sold per Product Category: (Enter: 6) ")
        print("                                  Exit Program: (Enter: 0) ")
        print("-----------------------------------------------------------")
        revenue_list = revenue_each_product(sales)
        total_revenue = total_rev(revenue_list)
        command = input("Command: ").strip()
        match command:
            case "1":
                sort = top_freq_p(sales)
                for i in range(len(sort)):
                    print(f"{sort[i][0]}: {sort[i][1]}pcs")
                input("Press Enter to go back to Menu")
            case "2":
                revenue_list = revenue_each_product(sales)
                for item in revenue_list:
                    print(
                        f"Product {item[0].title()} - Generated ${item[1]:.1f}")
                input("Press Enter to go back to Menu")
            case "3":
                total_revenue = total_rev(revenue_list)
                print(f"Total Revenue: ${total_revenue}")
                input("Press Enter to go back to Menu")
            case "4":
                print(average_revenue(sales, total_revenue))
                input("Press Enter to go back to Menu")
            case "5":
                sorted_rev_category_list = revenue_per_category(sales)
                for category in sorted_rev_category_list:
                    print(
                        f"Category {category[0].title()} generated ${category[1]:.1f}")
                input("Press Enter to go back to Menu")
            case "6":
                sorted_item_category_list = items_sold_per_category(sales)
                for category in sorted_item_category_list:
                    print(
                        f"Category {category[0].title()} sold {category[1]} Products")
                input("Press Enter to go back to Menu")
            case "0":
                sys.exit()


def check_file(check):
    if not check.endswith(".csv"):
        sys.exit("Must be a CSV-File!")


def readcsv(sales_csv):
    check_file(sales_csv)
    try:
        if not os.path.exists(sales_csv):
            raise FileNotFoundError
    except FileNotFoundError:
        sys.exit("File Not Found")
    sales = []
    with open(sales_csv) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",")
        for row in reader:
            sales.append(row)
        return sales


def top_freq_p(sales):
    freq = []
    for sale in sales:
        freq.append(sale["Product"])
    count = Counter(freq)
    countlist = []
    for product, frequency in count.items():
        countlist.append((product, frequency))
        sort = sorted(countlist, key=lambda tup: tup[1], reverse=True)
    return sort


def revenue_each_product(sales):
    products = {}
    for sale in sales:
        product = sale.get("Product")
        revenue = float(sale.get("Revenue"))
        if product not in products:
            products[product] = revenue
        else:
            products[product] += revenue
    sortedlist = []
    for name, generated_revenue in products.items():
        sortedlist.append([name, generated_revenue])
    sortedlist = sorted(sortedlist, key=lambda tup: tup[1], reverse=True)
    return sortedlist


def total_rev(revenue_list):
    total_revenue = 0
    for item in revenue_list:
        total_revenue += item[1]
    return f"{total_revenue:.1f}"


def average_revenue(sales, total_revenue):
    selling_dates = []
    for sale in sales:
        date_key = sale.get("Date")
        try:
            day, month, year = date_key.split("/")
        except ValueError:
            sys.exit("Wrong Dateformat! The Correct is DD/MM/YYYY, Check the File!")
        date_sold = date(int(year), int(month), int(day))
        selling_dates.append(date_sold)
    selling_dates = sorted(selling_dates)
    difference_in_time = selling_dates[len(
        selling_dates) - 1] - selling_dates[0]
    days = difference_in_time.days
    weeks = round(days/7, 2)
    months = round(days/30)
    print("What Average period would you like to see?")
    avg_period = input(
        "Enter \"1\" for /Day, \"2\" for /Week and \"3\" for /Month: ")
    match avg_period:
        case "1":
            return f"Average Revenue per Day is: {(total_revenue/days):.2f}"
        case "2":
            return f"Average Revenue per Week is: {(total_revenue/weeks):.2f}"
        case "3":
            return f"Average Revenue per Month is: {(total_revenue/months):.2f}"


def revenue_per_category(sales):
    category_list = {}
    for sale in sales:
        category = sale.get("Product Category")
        revenue = float(sale.get("Revenue"))
        if category not in category_list:
            category_list[category] = revenue
        else:
            category_list[category] += revenue
    sorted_category_list = sorted(
        category_list.items(), key=lambda x: x[1], reverse=True)
    return sorted_category_list


def items_sold_per_category(sales):
    category_list = {}
    for sale in sales:
        category = sale.get("Product Category")
        if category not in category_list:
            category_list[category] = 1
        else:
            category_list[category] += 1
    sorted_category_list = sorted(
        category_list.items(), key=lambda x: x[1], reverse=True)
    return sorted_category_list


if __name__ == "__main__":
    main()
