#import modules
import os
import csv

#set location of the election_data.csv
election_csv = os.path.join("PyPoll", 'Resources', "election_data.csv")

#total number of votes
total_Votes = 0

#set empty dictionary for the votes assign variables
votesPerCandidate = {}
candidate=[]
votes=[]

#open the election_data.csv file
with open(election_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Read the header row first

    for row in csvreader:
        total_Votes += 1
        if row[2] not in votesPerCandidate:
            votesPerCandidate[row[2]] = 1
        else:
            votesPerCandidate[row[2]] += 1   
        
#print statement
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_Votes))
print("-------------------------")

for candidate, votes in votesPerCandidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/total_Votes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

#return the winner using a max function of the dictionary 
winner = max(votesPerCandidate, key=votesPerCandidate.get)

#print statement for the winner
print(f"Winner: {winner}")

#set a location for the output to print (analysis.txt)
output_file =('PyPoll/Analysis/analysis.txt')

#open and write to the output file in write mode
with open(output_file,"w") as file:

    file.write("Election Results")
    file.write('\n')
    file.write("-------------------------")
    file.write('\n')
    file.write("Total Votes: " + str(total_Votes))
    file.write('\n')
    file.write("-------------------------")
    file.write('\n')

    for candidate, votes in votesPerCandidate.items():
        file.write(candidate + ": " + "{:.3%}".format(votes/total_Votes) + "   (" +  str(votes) + ")")
        file.write('\n')
        file.write("-------------------------") 
        file.write('\n')
        file.write(f"Winner: {winner}")
        file.write('\n')
