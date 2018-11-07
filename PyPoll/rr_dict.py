import os
import csv

#Path to collect data from the Resources folder
file_path = os.path.join("Resources", "election_data.csv")

#Global variables
candidates = {}

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

for row in rows:
    candidate = row[2]
    if candidate in candidates:
    if candidate in caindates.keys():
        count = candidates.get(candidate) + 1
        candidates.update({candidate:count})
        candidates[candidate] += 1
        candidate[candidate] = candidate[candidate] + 1
    else:
        candidates.update({candidate:1})
print(candidates)

for key, value in candidates.items():
    percentage_of_votes = round((value / total_votes * 100), 4)
    print(key, percentage_of_votes)

#Print data
print("Election Results")
print ("-------------------------")
print(f"Total Votes: {total_votes}")
print ("-------------------------")

for key, value in candidates.items():
    print("{}: ({})".format(key, value))

#print(f"Candidate1: {candidates['Khan']}")
#print(Candidate2 results)
#print(Candidate3 results)
#print(Candidate4 results)
print ("-------------------------")
print("Winner: TBD")

# with open(file_path) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     for i, row in enumerate(csvreader):
#         if i==0:
#             header = row
#         else:
#             dict = {rows[0]:rows[2] for rows in csvreader}
#     total_votes = len(dict)


# for key, value in candidates.items():
#     print("{}{}".format(key, value))