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
    print(rows[:3])

for row in rows:
    if 

#Print data
print("Election Results")
print ("-------------------------")
print(f"Total Votes: {total_votes}")
print ("-------------------------")
#print(Candidate1 results)
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