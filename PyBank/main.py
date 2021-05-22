#import dependencies
import csv
import os

#read in csv
py_bank_csv = os.path.join("Resources", "budget_data.csv")

#initialize variables
month_counter = 0
net_profit_loss = 0
avg_monthly_net = 0
greatest_increase_amt = 0
greatest_decrease_amt = 0
greatest_increase_month = ""
greatest_decrease_month = ""
output = ""

#open file and loop through rows
with open(py_bank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #count all rows
        month_counter += 1

        #str to int for calculations
        current_profit_losses = int(row[1])

        #sum all profits/losses
        net_profit_loss += current_profit_losses

        #save if current row haS greatest/least profits/losses
        if current_profit_losses > 0:
            if current_profit_losses > greatest_increase_amt:
                greatest_increase_amt = current_profit_losses
                greatest_increase_month = row[0]
        elif current_profit_losses < 0:
            if current_profit_losses < greatest_decrease_amt:
                greatest_decrease_amt = current_profit_losses
                greatest_decrease_month = row[0]

#avg_monthly_pro_lo = total_pro_lo / month_count
avg_monthly_net = net_profit_loss / month_counter

#output
output = "Financial Analysis \n" 
output += "----------------------------" + "\n"
output += "Total Months: " + str(month_counter) + "\n" 
output += "Total: $" + str(net_profit_loss) + "\n"
output += "Average Change: $" + str(round(avg_monthly_net, 2)) + "\n"
output += "Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str (greatest_increase_amt) +")" + "\n"
output += "Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease_amt) +")" + "\n"

print (output)

#writes output to txt file
output_file = os.path.join("analysis", "results.txt")
with open(output_file, "w") as datafile:
    datafile.write(output)