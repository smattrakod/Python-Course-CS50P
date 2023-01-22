# **Store-Sales-Analysis**

## **Video Demo:** <URL HERE>

---

# **Description:**

## **Short Summary:**

The Project is asking the user to input a csv-file containing sales data from a store. It can then calculate things such as: The product or product-category that generated most revenue, the total revenue, the average revenue per day/week or month or the most popular product/product-category.

## **CSV-File:**

For the script to fully work it is expected to be a csv-file in the directory which follows the criteria listed below. For inspiration on how an input file could look I have made a file called sales.csv. But the csv-file could be much larger and from a real store as long as it follows the correct format.

### **File-Columns:**

**- Date:** Is expected to be a string in format "DD/MM/YYYY"

**- Product:** Is expected to be a string with the name of any product.

**- Product Category:** Is expected to be a string with the name of any product-category.

**- Price:** Is expected to be a float value of the selling-price of the corresponding product.

**- Revenue:** Is expected to be a float value of the revenue from selling the product.

## **Functions:**

### **check_file(check):**

The Check_file is checking if it’s a csv_file. If the file does not end with
“.csv” it will exit the program and output a string that says “Must be a CSV-File!”.

### **readcsv(sales_csv):**

This function is taking a csv file as argument. If the file is not in the directory it will exit the program and output “File Not Found”. The readcsv(sales_csv) is assuming that the file is a csv file which contains the following five Columns: Date, Product, Product Category, Price, Revenue. In the code it is not any code that checks whether the code is fulfilling the requirements. So, the user will be expected to provide a correct file. The file is then read with the csv.DictReader(). This and appends all the rows from the csv-file to an empty list called sales. The list of dictionaries called sales is then being returned from the function.

### **top_freq_p(sales):**

This function is taking the list of dictionaries returned from readcsv() as argument and is then counting the frequency of different products. (I later found a easier way to perform this task but I didn’t wanna change it because I though it was good to learn multiple ways.) The function is then returning the sorted list of the most frequent products.

### **revenue_each_product(sales):**

This function also takes the return-value from readcsv() as input argument. It then iterates over all the dictionaries in the list and each time the product appears it add the revenue to the value in a new dictionary called “products”.
Afterward it creates a new list with the key:value pairs from the newly created dictionary. Then the list gets sorted with the sorted-function and with a lambda-function as a key argument. This makes it possible to sort dictionary key:value pairs based on the value. Because usually the sorted-function sort it based on the key.

### **total_rev(revenue_list):**

This function takes the return value from revenue_each_product() function as argument called revenue_list. Then for each value in the revenue_list it adds the revenue to the total_revenue. It then returns the total revenue with one decimal.

### **average_revenue(sales, total_revenue):**

it takes the return value from readcsv() and the return value from total_rev() as arguments. From sales it takes all the values from the Date-column and checks if the dateformat is correct. If the format is correct, it then converts all the dates to date-objects and appends them to a list called selling_dates. Then it sorts the list. After that it takes the different in time between the first date and the last date and calculates how many days it is. When that is done it asks the user if they want to know the average revenue per month/week or day. Depending on the answer the function will divide the total revenue with number of months, weeks or days in the period.

### **revenue_per_category(sales) & items_sold_per_category(sales):**

works very similar to revenue_each_product() but they are a little bit more refined because I learned a smoother way of doing the similar thing.

# **Testing the project:**

In the project there is also a file which test three of the functions. The functions that are being tested are: total_rev(), test_check_file() and test_readcsv().
