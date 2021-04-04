def PyPoll(input_path,output_path):
    import csv
    
    #Analyze the data
    with open(datalocation,"r") as temp: 
        electiondata = csv.reader(temp, delimiter=",") # read in the CSV file  
        headers = next(electiondata) # store headers
        print(f'Headers: {headers}')
        candidatelist = {}
        for rows in electiondata:
            if rows[2] in candidatelist.keys():
                candidatelist[rows[2]]+=1
            else:
                candidatelist[rows[2]] = 1
                   
        totalvotes = sum(candidatelist.values())
        winner = [candidate for candidate,votes in candidatelist.items() if votes == max(candidatelist.values())]
        
    # Format the output of election results   
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