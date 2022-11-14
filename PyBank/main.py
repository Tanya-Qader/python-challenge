#import modules 
import csv
import os

#setting the path for the csv file under resources folder
budget_csv = os.path.join("PyBank",'Resources','budget_data.csv')

#open the csv file to read the data
with open(budget_csv, "r") as csvfile:

    #store the content of budget_data.csv file in the csvreader variable
    csvreader = csv.reader(csvfile)

    #start with the next header to avoid the header lables
    header =next(csvreader)

    #create empty lists to iterate through specific rows
    total_months = []
    total_profit = []
    monthly_profit_change = []

    #iterate through the dataset and add these values to the empty lists
    for row in csvreader:
        total_months.append(row[0]) 
        total_profit.append(int(row[1]))

    #iterate through profits to find the monthly profit change
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

#evaluate the max and min from the list
increase_value =max(monthly_profit_change)
decrease_value =min(monthly_profit_change)

#using the index
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

#print all statements
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(decrease_value))})")

#set location of the output results
output_file =('PyBank/Analysis/financial_analysis.txt')
#write changes to the output file
with open(output_file,"w") as file:

        file.write(f"Financial Analysis")
        file.write("\n")
        file.write("----------------------------")
        file.write("\n")
        file.write(f"Total Months: {len(total_months)}")
        file.write("\n")
        file.write(f"Total: ${sum(total_profit)}")
        file.write("\n")
        file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
        file.write("\n")
        file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(increase_value))})")
        file.write("\n")
        file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(decrease_value))})")
