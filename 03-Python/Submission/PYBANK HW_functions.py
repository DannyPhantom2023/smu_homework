import csv
#Print the header
print("Financial Analysis")
print("----------------------------")

is_first_row=True
months=0               #Get all variables
total_profit=0
last_month_profit=0
changes=[]
# max change
# max month
max_change = -99999999999
max_month = ""

# min change
# min month
min_change = 999999999999999999
min_month = ""

#Import Csv, Csv Reader, and Header
bank_csv ="PyBank/Resources/budget_data.csv"
with open(bank_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        profit=int(row[1]) #add up profit
      
        if is_first_row:
            last_month_profit=profit
            is_first_row=False
            
            
        else:
            change=profit-last_month_profit
            changes.append(change)  
            
            last_month_profit=profit 
            if change > max_change:
                 max_change = change
                 max_month = row[0]

            if change < min_change:
                min_change = change
                min_month = row[0]

            
            
                     #Figure out a way to add up the months
        months +=1 
        total_profit+=int(row[1])
avg_change=sum(changes)/len(changes) #The average change is by subtracting current month by prior, then adding the total of all the changes made each month then divide by the total number of monthly changes
        
 #Then print them using f-strings       
print(f"Total Months: {months}")
print(f"Total: {total_profit}")
print(f"Average Change: {avg_change}")      
print(f"Greates Increase in Profits: {max_month}, (${max_change})")
print(f"Greatest Decrease in Profits:{min_month}, (${min_change})")
      



