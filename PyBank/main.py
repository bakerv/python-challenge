def PyBank(filepath,outputpath):
    # Dependencies
    import csv

    # Get operating parameters from the data set
    months = 0
    netprofit = 0
    date = []
    monthlyprofits = []
    with open(filepath) as temp:
        budgetdata = csv.reader(temp,delimiter=",") # Read in the CSV file
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
     
    # The greatest losses over the entire period
    minvalue = 0
    mindate = ""
    for x in range(months):
        if int(monthlyprofits[x]) < minvalue:
                minvalue = int(monthlyprofits[x])
                mindate = str(date[x])
    
    # The average of the changes in profit/losses over the entire period
    average = (round(netprofit/months,2))
    
    # Output to terminal
    print(f'''Profit Analysis
----------------------
Time Period: {months} months
Net Profit: ${netprofit}
Average Profit: ${average}
Greatest gain: {maxdate} ${maxvalue}
Greatest loss: {mindate} ${minvalue}''')
    
    #Output to text file
    import sys
    defaultout = sys.stdout
    with open(outputpath,'w') as text:
        sys.stdout = text
        print(f'''Profit Analysis
----------------------
Time Period: {months} months
Net Profit: ${netprofit}
Average Profit: ${average}
Greatest gain: {maxdate} ${maxvalue}
Greatest loss: {mindate} ${minvalue}''')
    sys.stdout = defaultout

# Call PyBank
import os

datalocation = os.path.join('Resources','budget_data.csv')
saveto = os.path.join('Analysis','PyBank_Output.txt')

PyBank(datalocation,saveto)