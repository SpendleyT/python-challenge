import os
import csv

#read-file path
budget_csv = os.path.join("Resources", "budget_data.csv")
#write-file path
file_path=os.path.join("Resources", "PyBank-Analysis.txt")

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #variable declarations
    total_months = 0
    total_profit = 0
    total_change = 0
    high_profit = 0
    high_profit_date = ""
    low_profit = 0
    low_profit_date = ""
    curr_profit = 0
    curr_change = 0
    start_profit = 0
    
    #read first row and set start value
    start_row = next(csvreader)
    total_months += 1 
    last_profit = curr_profit
    curr_profit = int(start_row[1])
    total_profit += curr_profit
    start_profit = curr_profit
    
    #process file rows and calculate results
    for row in csvreader:
        #read row data and calculate total profit
        total_months += 1 
        last_profit = curr_profit
        curr_profit = int(row[1])
        total_profit += curr_profit
        
        # Calculate row change and total change
        curr_change = (curr_profit - last_profit)
        total_change += curr_change
            
        #If high (or) low change, capture amount and date
        if curr_change > 0 and curr_change > high_profit:
            high_profit = curr_change
            high_profit_date = row[0]
        if curr_change < 0 and curr_change < low_profit:
            low_profit = curr_change
            low_profit_date = row[0]

#calculate average for profit changes
avg_change = round((curr_profit - start_profit) / (total_months - 1), 2)

#print results to terminal
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${avg_change} ")
print(f"Greatest Increase in Profits: {high_profit_date} (${high_profit})")
print(f"Greatest Decrease in Profits: {low_profit_date} (${low_profit})")

#print results to file
with open(file_path, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("-----------------------------\n")
    output.write(f"Total Months: {total_months}\n")
    output.write(f"Total: ${total_profit}\n")
    output.write(f"Average Change: ${avg_change}\n")
    output.write(f"Greatest Increase in Profits: {high_profit_date} (${high_profit})\n")
    output.write(f"Greatest Decrease in Profits: {low_profit_date} (${low_profit})\n")


