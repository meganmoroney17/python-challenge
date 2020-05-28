import os
import csv

poll_csv = r"C:\Users\megan.moroney\Desktop\python-challenge\PyPoll\Resources\Election_data.csv"

def results(data):

    totalvotes = 0
    votes = []
    candidates = []
    uniquecandidates = []
    percent = []
     
    for row in data:

        totalvotes += 1

        if row[2] not in uniquecandidates:
            uniquecandidates.append(row[2])

        votes.append(row[2])

    for candidate in uniquecandidates:
        candidates.append(votes.count(candidate))
        percent.append(round(votes.count(candidate)/totalvotes*100,3))

    winner = uniquecandidates[candidates.index(max(candidates))]
    
    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {totalvotes}')
    print('--------------------------------')
    for i in range(len(uniquecandidates)):
        print(f'{uniquecandidates[i]}: {percent[i]}% {candidates[i]}')
    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')

    output = os.path.join("PyPollResults.txt")

    with open(output, "w") as txtfile:
        txtfile.write('Election Results')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nTotal Votes: {totalvotes}')
        txtfile.write('\n------------------------------------')
        for i in range (len(uniquecandidates)):
            txtfile.write(f'\n{uniquecandidates[i]}: {percent[i]}% {candidates[i]}')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nWinner: {winner}')
        txtfile.write('\n------------------------------------')


with open(poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    
    results(csvreader)