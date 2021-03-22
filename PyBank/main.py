import os
import csv
budgetcsv=os.path.join("Resources","budget_data.csv")
monthcount=0
netgain=0
avggain=0
monthcount=0
maxgain=0
maxloss=0
previousvalue=0
changelist=[]

with open(budgetcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader=next(csvreader)
    for row in csvreader:
        currentgain=int(row[1])
        currentmonth=row[0]


        netgain+=currentgain
        monthcount+=1
        if currentgain>maxgain:
            maxgain=currentgain
            maxmonth=currentmonth
        if currentgain<maxloss:
            maxloss=currentgain
            lossmonth=currentmonth
        
        changelist.append(currentgain-previousvalue)
        previousvalue=currentgain
    avggain=netgain/monthcount
avggain=sum(changelist)/len(changelist)
finanicalreport=f"Financial Analysis\n=====================\nTotal Months: {monthcount}\nTotal: ${netgain}\nAverage Change: ${avggain}\nGreatest Increase in Profits: {maxmonth} (${maxgain})\nGreatest Decrease in Losses: {lossmonth} (${maxloss})"
print(finanicalreport)

reportfile=os.path.join("Analysis","Financial Report.txt")

with open(reportfile,"w",newline="\n") as datafile:
    datafile.write(finanicalreport)
    datafile.close()

