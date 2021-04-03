import os
import csv
numrows = 0
uniquenames = set()

file_path = os.path.join("Resources","election_data.csv")
with open(file_path,"r") as temp:
    electiondata = csv.reader(temp, delimiter=",")

    for rows in electiondata:
        numrows += 1
        uniquenames.add(rows[2])
        
totalvotes = numrows - 1
uniquenames.remove("Candidate")
candidates = list(uniquenames)
votes = [0] * len(candidates)
print(f'votes: {votes}')

# count votes
with open(file_path,"r") as temp:
    electiondata = csv.reader(temp, delimiter=",")
    
    for rows in electiondata:
        for names in candidates:
            if rows[2] == names:
                votes[candidates.index(names)] +=1

percentvotes = [round((x/totalvotes)*100,2) for x in votes]                       
print(totalvotes)
print(candidates)
print(votes)
print(percentvotes) 
  
#%%

# The winner of the election based on popular vote
