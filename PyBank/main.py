# Dependencies
import os
import csv

# Locate the data set
filepath = os.path.join("Resources","budget_data.csv")
months = 0
netprofit = 0
date = []
monthlyprofits = []
# Get operating parameters from the data set
with open(filepath) as temp:
    budgetdata = csv.reader(temp,delimiter=",")
    headers = next(budgetdata)     
    for rows in budgetdata:
        months += 1 
        date.append(rows[0])
        monthlyprofits.append(rows[1])
   
# Net profit function        
for x in range(months):
    netprofit = netprofit + int(monthlyprofits[x])

# The greatest increase in profits over the entire period
maxvalue = 0
maxdate = ""
for x in range(months):
    if int(monthlyprofits[x]) > maxvalue:
        maxvalue = int(monthlyprofits[x])
        maxdate = str(date[x])
        
minvalue = 0
mindate = ""
# the greatest decrease in losses over the entire period
for x in range(months):
    if int(monthlyprofits[x]) < minvalue:
            minvalue = int(monthlyprofits[x])
            mindate = str(date[x])

average= (round(netprofit/months,2))
# The average of the changes in profit/losses over the entier period


# print to terminal
print(f'''Profit Analysis
----------------------
Time Period: {months} months
Net Profit: ${netprofit}
Average Profit: ${average}
Greatest gain: {maxdate} ${maxvalue}
Greatest loss: {mindate} ${minvalue}''')

#export results 
import sys
defaultout = sys.stdout
with open('Analysis\PyBank_output.txt','w') as text:
    sys.stdout = text
    print(f'''Profit Analysis
    ----------------------
    Time Period: {months} months
    Net Profit: ${netprofit}
    Average Profit: ${average}
    Greatest gain: {maxdate} ${maxvalue}
    Greatest loss: {mindate} ${minvalue}''')
sys.stdout = defaultout
