# dependencies
import os
import csv


# Get operating parameters from the data set
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

# Count the votes
candidates = list(uniquenames)
votes = [0] * len(candidates)

with open(file_path,"r") as temp:
    electiondata = csv.reader(temp, delimiter=",")
    for rows in electiondata:
        for names in candidates:
            if rows[2] == names:
                votes[candidates.index(names)] +=1

# convert votes to percentage
percentvotes = [round((x/totalvotes)*100,2) for x in votes]                       

# determine the position of the winner
winner = votes.index(max(votes))  

# Output to terminal
print(f'''Fictional State Election Results
--------------------------------
Total Votes: {totalvotes}
--------------------------------''')
for person in candidates:
    x = candidates.index(person)
    print(f'{candidates[x]}: {percentvotes[x]}% ({votes[x]})')
print(f'''--------------------------------
Winner: {candidates[winner]}''')

#Output to text file
print(f'''Fictional State Election Results
--------------------------------
Total Votes: {totalvotes}
--------------------------------''')
for person in candidates:
    x = candidates.index(person)
    print(f'{candidates[x]}: {percentvotes[x]}% ({votes[x]})')
print(f'''--------------------------------
Winner: {candidates[winner]}''')

