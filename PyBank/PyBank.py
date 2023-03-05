# import necessary libraries
import csv

# Initialize output file name and budget data list so that the data is accessible outside 'with' statement
output_file = 'PyBank.txt'
budget_data = []

# define a function to find the date of any particular change given:
# a 'data_set', changes in pnl ('pnl_diffs') and the 'change' we're looking for
def date_of_pnl_change(data_set, pnl_diffs, change):
    """
    Returns the date that the 'change' happened from the 'data_set'
    
    Parameters
    ----------
    dataset : list
        data read in from csv
    pnl_diffs : list
        diffences (amount of change) in Profits and Losses (PnL)
    change : int
        the particular change in PnL you're looking for
    """
    
    # loop through the dates from the data set and changes in PnL together and return
    # the date only if it matches the particular 'change' in PnL we're looking for.
    # Since the date is returned as a single element list, take only that element.
    change_date = [date[0] for date,pnl in zip(data_set[1:],pnl_diffs) if pnl == change][0]
    return change_date

# load data from provided csv. We know what the data looks like: 2 cols, multiple rows
with open('budget_data.csv') as csv_file:
    bank_data_set = csv.reader(csv_file)
    header = next(bank_data_set)
    
    # We loop through each row of the dataset, we set the first column to the date
    # and the 2nd column to the PnL as an integer
    budget_data = [[data[0], int(data[1])] for data in bank_data_set]

# The total number of months included in the dataset
total_months = len(budget_data)

# The net total amount of Profit/Losses over the entire period
pnls = [pnl[1] for pnl in budget_data]
net_total_pnl = sum(pnls)

# The average of the changes in Profit/Losses over the entire period
#  1. first get the changes by subtracting a copy of the PnLs from the PnLs offset
#     from the first row since there's no data before the first row/date
pnl_changes = [x - y for x,y in zip(pnls[1:], pnls)]
average_change_in_pnl = round(sum(pnl_changes)/len(pnl_changes), 2)

# The greatest increase in profits (date and amount) over the entire period
max_incr_in_profits = max(pnl_changes)
date_of_max_incr_in_profits = date_of_pnl_change(budget_data, pnl_changes, max_incr_in_profits)

# The greatest decrease in losses (date and amount) over the entire period
max_decr_in_profits = min(pnl_changes)
date_of_max_decr_in_profits = date_of_pnl_change(budget_data, pnl_changes, max_decr_in_profits)

# print out stats: 1. stdout, 2. file
# 0. Create string to be outputted
stats = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total_pnl}
Average  Change: ${average_change_in_pnl:.2f}
Greatest Increase in Profits: {date_of_max_incr_in_profits} (${max_incr_in_profits})
Greatest Decrease in Profits: {date_of_max_decr_in_profits} (${max_decr_in_profits})
"""

# 1. stdout (output to screen)
print(stats)

# 2. output to file
with open(output_file, 'w') as of:
    of.write(stats)
