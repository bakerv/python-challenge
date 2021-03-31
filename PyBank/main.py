data = open(Resources\'Budget_data.csv')
# Objectives

# Total number of months in the data set
#   Use the len function to count the number of rows in the data set
months = len(datasetrows) or rows(data) 
#The net total amount of pofit losses over the entier period 
#Summation of all rows column 2
netprofit = 0
 For x in range(1,months+1):
     netprofit = netprofit + x,column2

# The average of the changes in profit/losses over the entier period
average= netprofit/months

#The greatest increase in profits over the entire period
max = 0
For x in range(1,months+1):
    If x > max:
        max = x
 min = 0       
# the greatest decrease in losses over the entire period
    For x in range(1,months+1):
        If x < min:
            min = x
# print to terminal
#export results 