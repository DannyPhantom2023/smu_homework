import  csv

votes = 0
#Import Csv,reader, and header
candidates = {}
poll_csv ="PyPoll/Resources/election_data.csv"
with open(poll_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
       

        votes += 1

        # get the candidate
        # if the candidate is in the dictionary, we want to add 1 to the value
        # else, init with a vote of one

        candidate = row[2]
        if candidate in candidates.keys():
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
winner=max(candidates,key=candidates.get)

output=f"""Election Results
--------------------------

Total Votes: {votes}

---------------------------\n"""
for key in candidates.keys():
    perc= round(100*candidates[key]/votes, 3)
    newline=f"{key}:{perc}% ({candidates[key]})\n"
    output += newline
lastline=f"""--------------------
Winner:{winner}
--------------------"""
output+=lastline
print(output)
