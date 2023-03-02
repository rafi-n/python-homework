# import necessary libraries
import pandas as pd

# Initialize output file name
output_file = 'PyBank.txt'

# load data from provided csv. We know what the data looks like: 2 cols, multiple rows
bank_data_set = pd.read_csv('budget_data.csv')
headers = bank_data_set.columns
date_header = headers[0]
pnl_header = headers[1]

# The total number of months included in the dataset
total_months = len(bank_data_set)

# The net total amount of Profit/Losses over the entire period
net_total_pnl = sum(bank_data_set[pnl_header])

# The average of the changes in Profit/Losses over the entire period
# first get the changes
changes_in_pnl = bank_data_set.set_index(date_header).diff()
# NOTE: changes_in_pnl first difference is NaN because it has no previous month to compare to
# As a result, we compare 1 month less than the total (i.e. total_months - 1)
total_change_in_pnl = sum(changes_in_pnl[pnl_header][1:])
average_change_in_pnl = total_change_in_pnl / (total_months - 1)

# The greatest increase in profits (date and amount) over the entire period
max_incr_in_profits = changes_in_pnl.max().values[0]
date_of_max_incr_in_profits = changes_in_pnl.idxmax().values[0]

# The greatest decrease in losses (date and amount) over the entire period
max_decr_in_profits = changes_in_pnl.min().values[0]
date_of_max_decr_in_profits = changes_in_pnl.idxmin().values[0]

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
