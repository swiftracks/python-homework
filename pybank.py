# Import the pathlib and csv library
from pathlib import Path
import csv


csvpath = Path('budget_data.csv')

months = []
profit_losses = []
greatest_increase_amount = 0
greatest_decrease_amount = 0

greatest_increase_date = ""
greatest_decrease_date = ""

line_num = 0

# Open the input path as a file object
with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    line_num += 1
    
    print(f"{header} <---- HEADER")
    
    previous_pl = int(row[1])

    for row in csvreader:
        
        month = row[0]
        pl_amount = int(row[1])
        
        months.append(month)
        profit_losses.append(pl_amount)
        
        if(pl_amount > previous_pl and pl_amount > greatest_increase_amount):
            greatest_increase_amount = pl_amount
            greatest_increase_date = month
        elif(pl_amount < previous_pl and pl_amount < greatest_decrease_amount):
            greatest_decrease_amount = pl_amount
            greatest_decrease_date = month
            
        
        previous_pl = pl_amount
        
        
print("Financial Analysis")

print("-------------------------")
        
total_months = len(months)
print(f"Total months: {total_months}")

total_net = sum(profit_losses)
print(f"Total: ${total_net}")

avg = total_net / total_months
formatted_avg = "{:.2f}".format(avg)
print(f"Average Change: ${formatted_avg}")

print(f"Greatest increase in profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest decrease in profits: {greatest_decrease_date} (${greatest_decrease_amount})")