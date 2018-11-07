import os
import csv

#Path to collect data from the Resources folder
file_path = os.path.join("Resources", "election_data.csv")

#Global variables
candidates = {}
percent = {}

#Import the election_data.csv file into the rows dictionary
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    rows = []
    for i, row in enumerate(csvreader):
        if i==0:
            header = row
        else:
            rows.append(row)
    total_votes = len(rows)

#Store candidates in a dictionary and count the number of votes per candidate
for row in rows:
    candidate = row[2]
    if candidate in candidates:
        candidates[candidate]["votes"] += 1
    else:
        candidates[candidate] = {"votes": 1}
#print(candidates)

#Calculate the percent of votes and update the dictionary
for key, value in candidates.items():
    ind_votes = candidates.get(key, {}).get("votes")
    percentage_of_votes = round((ind_votes / total_votes * 100), 3)
    candidates[key] = {"votes":ind_votes, "percent_votes": percentage_of_votes}
#print(candidates)


#Print data
print("Election Results")
print ("-------------------------")
print(f"Total Votes: {total_votes}")
print ("-------------------------")

for key, value in candidates.items():
    print(f"{key}: {value['percent_votes']}% ({value['votes']})")
print ("-------------------------")


# v=list(candidates["votes"].values())
# print(v)
# winner = list(candidates.keys())[v.index(max(v))]   


winner = max(int(d['votes']) for d in candidates.values())
print(f"Winner: {winner}")







