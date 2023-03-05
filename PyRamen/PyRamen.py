# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('./Resources/menu_data.csv')
sales_filepath = Path('./Resources/sales_data.csv')
# create output file
report_file = Path('./PyRamen.txt')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# define function to read a csv to a list
def read_csv_to_list(input_csv_file):
    """
    Read a CSV file to a list
    
    Parameters:
    -----------
    input_csv_file : file
    """
    
    output_list = []
    # Use try/except statement to give 'soft landing' instead of crashing
    # if the file is not found
    try:
        with open(input_csv_file, 'r') as input_file:
            input_csv = csv.reader(input_file)
            next(input_csv)
            for item in input_csv:
                output_list.append(item)
    except FileNotFoundError:
        print(f"File: {input_csv_file} not found!")
    return output_list

# @TODO: Read in the menu data into the menu list
menu = read_csv_to_list(menu_filepath)

# @TODO: Read in the sales data into the sales list
sales = read_csv_to_list(sales_filepath)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for item in sales:

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    line_item_id = item[0]
    date = item[1]
    cc_num = item[2]
    quantity = int(item[3])
    sales_item = item[4]
    
    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if sales_item not in report:
        report[sales_item] = {
            "01-count":0,
            "02-revenue":0,
            "03-cogs":0,
            "04-profit":0
        }

    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for record in menu:

        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        menu_item = record[0]
        menu_cat = record[1]
        menu_desc = record[2]
        menu_price = float(record[3])
        menu_cost = float(record[4])

        # @TODO: Calculate profit of each item in the menu data
        profit = menu_price - menu_cost

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if sales_item == menu_item:

            # @TODO: Print out matching menu data
            print(f"\n-------------------\n{record}\n-------------------\n")

            # @TODO: Cumulatively add up the metrics for each item key
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += menu_price * quantity
            report[sales_item]["03-cogs"] += menu_cost * quantity
            report[sales_item]["04-profit"] += profit * quantity

        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        else:
            print(f"{sales_item} does not equal {menu_item}! NO MATCH!")


    # @TODO: Increment the row counter by 1
    row_count += 1

# @TODO: Print total number of records in sales data
print(f"Total number of records in sales data: {row_count}")

# @TODO: Write out report to a text file (won't appear on the command line output)
with open(report_file, 'w') as op_file:
    for key,val in report.items():
        op_file.write(f"{key} {val}\n")