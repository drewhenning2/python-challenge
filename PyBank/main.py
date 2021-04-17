# import modules
import os
import csv

# change directories
py_bank_csv = os.path.join("Resources", "budget_data.csv")

# open csv file in read mode
with open(py_bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
# skip the header row 
    next(csvreader)

# create empty lists because the budget_data.csv does not have all the data we need to complete the calculations
    total_months = []
    total_profit = []
    monthly_change = []

# loop through the rows and add (append) them to the empty lists from above
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    for i in range(len(total_profit)-1):
        monthly_change.append(total_profit[i+1]-total_profit[i])

# calculate average change
    average_change = round(sum(monthly_change)/(len(total_months) - 1), 2)

# calculate max
    greatest_increase = max(monthly_change)
    max_index = monthly_change.index(greatest_increase)
    max_date = total_months[max_index+1]

# calculate min
    greatest_decrease = min(monthly_change)
    min_index = monthly_change.index(greatest_decrease)
    min_date = total_months[min_index+1]

# print to terminal
print(f'''
Financial Analysis
------------------------
Total Months: {len(total_months)}
Total Net Profit/Loss: ${sum(total_profit)}
Average Change: ${average_change}
Greatest Increase in Profits: {max_date} ${greatest_increase}
Greatest Decrease in Profits: {min_date} ${greatest_decrease}
''')

# export to txt file
output_file_path = os.path.join("Analysis", 'finanacial_analysis.txt')
with open(output_file_path, 'w') as output_file:

    output_file.write("Financial Analysis")
    output_file.write("\n")

    output_file.write("------------------------")
    output_file.write("\n")

    output_file.write(f"Total Months: {len(total_months)}")
    output_file.write("\n")

    output_file.write(f"Total Net Profit/Loss: ${sum(total_profit)}")
    output_file.write("\n")

    output_file.write(f"Average Change: ${average_change}")
    output_file.write("\n")

    output_file.write(f"Greatest Increase in Profits: {max_date} ${greatest_increase}")
    output_file.write("\n")

    output_file.write(f"Greatest Decrease in Profits: {min_date} ${greatest_decrease}")