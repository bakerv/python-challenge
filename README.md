# **Python-Challenge**

This repository contains two functions developed to complete basic accounting tasks, and count election votes.

## **PyBank()**
PyBank is a basic accounting function. Given dates and figures associated with those date, PyBank will output the sum, mean, min, and max of the data set.  The output is displayed in the terminal, and written to a specified location.
 
![PyBank](https://github.com/bakerv/python-challenge/blob/main/PyBank/Images/Sample.PNG)

### *Data Format*
Data should be in two columns (Months),(Profit). With months as the first column, and the profit/loss for that month as the second column

## **PyPoll()**
PyPoll is a vote counting function. PyPoll uses the python dictionary function to sort through and tally a data column of names, determine the frequecny each occurs, and declare a winner for the election.

![PyPoll](https://github.com/bakerv/python-challenge/blob/main/PyPoll/Images/Sample.PNG)
### *Data Format*
The votes should be in the third column of the data set. Currently, the information in the first two columns is not used. Future development will implement voter ID tracking to ensure a person only votes once, as well as a county level information breakdown.