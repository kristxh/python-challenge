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

for row in rows:
    candidate = row[2]
    if candidate in candidates:
        candidates[candidate]["votes"] += 1
    else:
        candidates[candidate] = {"votes": 1}
#print(candidates)

for key, value in candidates.items():
    ind_votes = candidates.get(key, {}).get("votes")
    percentage_of_votes = round((ind_votes / total_votes * 100), 4)
    percent[key] = {"percent_votes": percentage_of_votes}
candidates.update(percent)
print(candidates)


# for pet_name, pet_information in pets.items():
#     print("\nHere is what I know about %s:" % pet_name.title())
#     # Each animal's dictionary is in 'information'
#     for key in pet_information:
#         print(key + ": " + str(pet_information[key]))

#Print data
print("Election Results")
print ("-------------------------")
print(f"Total Votes: {total_votes}")
print ("-------------------------")

# for key, value in candidates.items():
#     print("{}: ({})".format(key, value))


print ("-------------------------")
print("Winner: TBD")

