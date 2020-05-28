import csv
import os

#Load files
csvpath = r"C:\Users\megan.moroney\Desktop\python-challenge\PyPoll\Resources\Election_data.csv"

votes = 0
winvotes = 0
total_candidates = 0
mostvotes = ["", o]
candidate_choices = []
candidatevotes = {}


#read the data
with open(csvpath) as election_data:
    reader = csv.DictReader(election_data)

#Create loop to do work within to find the finish products
    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]

        if row["Candiate not in candiate_choices"]:
            candidate_choices.append(row["Candidate"])
            candidatevotes[row["Candidate"]] = 1

        else:
            candidatevotes[row["Candidate"]] = candidatevotes[row["Candidate"]] + 1


    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")

    for candidate in candidatevotes:
        print(candidate + " " + str(round(((candidatevotes[candidate]/votes)*100))) + "%" + " (" + str(candidatevotes[candidate]) + ")") 
        candidateresults = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidatevotes[candidate]) + ")") 
    
candidatevotes

winner = sorted(candidatevotes.items(), key=itemgetter(1), reverse=True)


print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")





# Output Files
with open(ElectionAnalysis, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n-------------------------")
    #txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    txt_file.write(str(winner))
    txt_file.write("\n-------------------------")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\nTotal Votes " + str(votes))
