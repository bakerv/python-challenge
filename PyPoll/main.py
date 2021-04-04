def PyPoll(input_path,output_path):
    import csv
    
    #Analyze the data, create a dictionary with candidate names as keys, and votes received as values
    with open(datalocation,"r") as temp: 
        electiondata = csv.reader(temp, delimiter=",") # read in the CSV file 
        
        #Store headers, and output to the terminal
        headers = next(electiondata) 
        print(f'Headers: {headers}')
        
        # Count the votes using a dictionary, determine counts of each unique value in the third column of the data set
        candidatelist = {}
        for rows in electiondata:
            if rows[2] in candidatelist.keys(): # Check if the candidate already has a key in the dictionary
                candidatelist[rows[2]] += 1 # add a vote to an existing key
            else:
                candidatelist[rows[2]] = 1 # Create a key in the dictionary if the candidate does not already have one
        
        # Determine the total votes cast in the election, and the winner    
        totalvotes = sum(candidatelist.values())
        winner = [candidate for candidate,votes in candidatelist.items() if votes == max(candidatelist.values())]
        
    # Output the election results in an organized format  
    def resultrecorder():      
        print(f'''Election Results
--------------------------------
Total Votes: {totalvotes}
--------------------------------''')
        for candidate in candidatelist:
            votes = candidatelist.get(candidate)
            percentvotes = round((votes/totalvotes)*100,2)
            print(f'{candidate}: {percentvotes}% {votes}')
        print(f'''--------------------------------
Winner: {str(winner).replace("[","").replace("'","").replace("]","")}''')
    # Output results to the terminal
    resultrecorder()
    
    # Output results to specified text file
    import sys
    defaultout = sys.stdout
    with open(output_path,'w') as text:
        sys.stdout = text
        resultrecorder()
    sys.stdout =defaultout

#Call PyPoll
import os

datalocation = os.path.join("Resources","election_data.csv")
saveto = os.path.join("Analysis","PyPoll_Output.txt")
PyPoll(datalocation,saveto)       