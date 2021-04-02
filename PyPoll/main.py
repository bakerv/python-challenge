# Objectives
import csv
open('Resources\election_data',"r") # change this to importing data filee using csv
# The total number of votes cast
votes = rows(dataset ) - 1

# A complete list of candidates who received votes
with dataset(column3):
    #identify unique values in this column, turn this column into a set? Yes read in the candidate column from the csv as a set to get unique values
    candidates = set(column3)
# the total number of votes each candidate won
whovotes[len(canditates)] = 0
with candidates(column3)
    for x in range(2,dataset rows +1):
       whovotes(candidates(x)) = whovotes(candidates(x)) +1
# the percentage of votes each candidate won
percentvotes = (whovotes/votes) * 100 #round this to 1 decimal

# The winner of the election based on popular vote
