import os
import csv

#Path to collect data from the Resources folder
file_path = os.path.join("Resources", "election_data.csv")

#Global variables
candidates = {}
percent_votes = {}

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
        candidates['votes'] += 1
    else:
        candidates.update({'name': [candidate], 'votes': 0})
print(candidates)

# for key, value in candidates.items():
#     percentage_of_votes = round((value / total_votes * 100), 4)
#     candidates['percent'] = {percentage_of_votes}
# print(candidates)

#Print data
print("Election Results")
print ("-------------------------")
print(f"Total Votes: {total_votes}")
print ("-------------------------")

for key, value in candidates.items():
    print("{}: ({})".format(key, value))


print ("-------------------------")
print("Winner: TBD")

