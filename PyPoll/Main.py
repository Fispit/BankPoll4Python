import os
import csv
import decimal


electionsheet=os.path.join("Resources","election_data.csv")
votecount={}
totalvotes=0


with open(electionsheet,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader=next(csvreader)

    for row in csvreader:
        candidatename=row[2]
        votecount[candidatename]=votecount.get(candidatename,0)+1
        totalvotes+=1







electionresults=f"Election Results\n====================\nTotal Votes: {totalvotes}\n====================\n"
winnervotes=0
for candidate in votecount:
    candidatevotes=votecount[candidate]
    percentagevote=round(candidatevotes/totalvotes*100,5)
    electionresults+=f"{candidate}: {percentagevote}% ({candidatevotes})\n"
    if candidatevotes>winnervotes:
        winner=candidate
        winnervotes=candidatevotes

electionresults+=f"====================\nWinner: {winner}\n===================="

print(electionresults)

outputloc=os.path.join("Analysis","Election Results.txt")
with open(outputloc,"w",newline="\n") as outputfile:
    outputfile.write(electionresults)
    outputfile.close()