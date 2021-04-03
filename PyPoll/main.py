# Function PyPoll, returns results from election data
def PyPoll(input_path,output_path):
    
    #Dependencies
    import csv
    
    # Get operating parameters from the data set
    totalvotes = 0
    uniquenames = set()
    with open(input_path,"r") as temp: 
        electiondata = csv.reader(temp, delimiter=",") # read in the CSV file  
        headers = next(electiondata) # store headers
        for rows in electiondata:
            totalvotes += 1
            uniquenames.add(rows[2])
 
    # Count the votes
    candidates = list(uniquenames)
    votes = [0] * len(candidates)
    with open(input_path,"r") as temp:
        electiondata = csv.reader(temp, delimiter=",")
        for rows in electiondata:
            for names in candidates:
                if rows[2] == names:
                    votes[candidates.index(names)] += 1
    
    # convert votes to percentage
    percentvotes = [round((x/totalvotes)*100,2) for x in votes]                       
    
    # determine the position of the winner
    winner = votes.index(max(votes))  
    
    # Output results to terminal
    print(f'''Fictional State Election Results
--------------------------------
Total Votes: {totalvotes}
--------------------------------''')
    for person in candidates:
        x = candidates.index(person)
        print(f'{candidates[x]}: {percentvotes[x]}% ({votes[x]})')
    print(f'''--------------------------------
Winner: {candidates[winner]}''')
    
    #Output results to text file
    import sys
    defaultout = sys.stdout
    with open(output_path,'w') as text:
        sys.stdout = text
        print(f'''Fictional State Election Results
--------------------------------
Total Votes: {totalvotes}
--------------------------------''')
        for person in candidates:
            x = candidates.index(person)
            print(f'{candidates[x]}: {percentvotes[x]}% ({votes[x]})')
        print(f'''--------------------------------
Winner: {candidates[winner]}''')
    sys.stdout = defaultout

# Call PyPoll
import os

datalocation = os.path.join("Resources","election_data.csv")
saveto = os.path.join("Analysis","PyPoll_Output.txt")

# PyPoll(datalocation,saveto)
import csv
with open(datalocation,"r") as temp: 
    electiondata = csv.reader(temp, delimiter=",") # read in the CSV file  
    headers = next(electiondata) # store headers
    candidatelist = {}
    for rows in electiondata:
        if rows[2] in candidatelist.keys():
            candidatelist[rows[2]]+=1
        else:
            candidatelist[rows[2]] = 1
    print(candidatelist)      
    # for rows in electiondata:
        
        

