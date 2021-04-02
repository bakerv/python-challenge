#%%
import os
import csv
# locate the data set
filepath = os.path.join("Resources","budget_data.csv")
months = 0
netprofit = 0
monthlyprofits = []
# read in the data set
with open(filepath) as temp:
    budgetdata = csv.reader(temp,delimiter=",")
    print(budgetdata)
    # iterate through each row    
    for rows in budgetdata:

        months = months + 1 # row counting, excludes header
        monthlyprofits.append(rows[1])
for x in range(1,months):
    netprofit = netprofit + int(monthlyprofits[x])
    

#%%
#The greatest increase in profits over the entire period
maxvalue = 0
for x in range(1,months):
    if int(monthlyprofits[x]) > maxvalue:
        maxvalue = int(monthlyprofits[x])
        
minvalue = 0
# the greatest decrease in losses over the entire period
for x in range(1,months):
    if int(monthlyprofits[x]) < minvalue:
            minvalue = int(monthlyprofits[x])
            
average= (round(netprofit/months,2))

print(months) #testing counter
print(monthlyprofit)
print(netprofit)  
print(minvalue)
print(maxvalue)
print(average)      

#%%

# The average of the changes in profit/losses over the entier period


# print to terminal
print("Profit Analysis")
print("----------------------")
print(f"Time Period: {months} months")
print(f"Net Profit: ${netprofit}")
print(f"Average Profit: ${average}")
print(f"Greatest gain: ${minvalue}")
print(f"Greatest loss: ${maxvalue}")
#export results 
import sys
defaultout = sys.stdout
with open('Analysis\pyBank_output.txt','w') as text:
    sys.stdout = text
    print("Profit Analysis")
    print("----------------------")
    print(f"Time Period: {months} months")
    print(f"Net Profit: ${netprofit}")
    print(f"Average Profit: ${average}")
    print(f"Greatest gain: ${minvalue}")
    print(f"Greatest loss: ${maxvalue}")
sys.stdout = defaultout
