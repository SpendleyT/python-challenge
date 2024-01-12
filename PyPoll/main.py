import os
import csv

#read-file path
election_csv = os.path.join("Resources", "election_data.csv")
#write-file path
file_path=os.path.join("Resources", "PyPoll_Results.txt")

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #declare variables - vote counts
    votes_stockham = 0
    votes_degette = 0
    votes_doane = 0
    votes_other = 0
    per_stockham = 0.0
    per_degette = 0.0
    per_doane = 0.0
    
    #process file rows and calculate results
    for row in csvreader:
        #process rows and count votes
        match row[2]:
            case "Charles Casper Stockham":
                votes_stockham += 1
            case "Diana DeGette":
                votes_degette += 1
            case "Raymon Anthony Doane":
                votes_doane += 1
            case _:
                votes_other += 1
    
    #Calc total votes
    votes_total = votes_stockham + votes_degette + votes_doane
    
    winner = ""
    #determine winner
    if votes_stockham > votes_degette:
        if votes_stockham > votes_doane:
            winner = "Charles Casper Stockham"
        else:
            winner = "Raymon Anthony Doane"
    else:
        if votes_degette > votes_doane:
            winner = "Diana DeGette"
        else:
            winner = "Raymon Anthony Doane"
    
    #Calc vote percentage per candidate
    per_stockham = votes_stockham / votes_total
    per_degette = votes_degette / votes_total
    per_doane = votes_doane / votes_total
    
    #print to screen
    print("Election Results")
    print("------------------------------------")
    print(f"Total Votes: {votes_total}")
    print("------------------------------------")
    print(f"Charles Casper Stockham: {per_stockham: .3%}  ({votes_stockham}) ")
    print(f"Diana DeGette: {per_degette: .3%}  ({votes_degette}) ")
    print(f"Raymon Anthony Doane: {per_doane: .3%}  ({votes_doane}) ")
    print("------------------------------------")
    print(f"Winner: {winner}")
    print("------------------------------------")
    
    #print to file
    with open(file_path, 'w') as output:
        output.write("Election Results\n")
        output.write("------------------------------------\n")
        output.write(f"Total Votes: {votes_total}\n")
        output.write("------------------------------------\n")
        output.write(f"Charles Casper Stockham: {per_stockham: .3%}  ({votes_stockham}) \n")
        output.write(f"Diana DeGette: {per_degette: .3%}  ({votes_degette}) \n")
        output.write(f"Raymon Anthony Doane: {per_doane: .3%}  ({votes_doane}) \n")
        output.write("------------------------------------\n")
        output.write(f"Winner: {winner}\n")
        output.write("------------------------------------\n")