import os
import csv

#Path to collect data from the Resources folder
file_path = os.path.join("Resources", "election_data.csv")

#Global variables
candidates = {}
percent = {}
winner_name = ""

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

#Calculate the percent of votes and update the dictionary
for key, value in candidates.items():
    ind_votes = candidates.get(key, {}).get("votes")
    percentage_of_votes = round((ind_votes / total_votes * 100), 3)
    candidates[key] = {"votes":ind_votes, "percent_votes": percentage_of_votes}

#Print data
print("Election Results")
print ("-------------------------")
print(f"Total Votes: {total_votes}")
print ("-------------------------")

for key, value in candidates.items():
    print(f"{key}: {value['percent_votes']}% ({value['votes']})")
print ("-------------------------")

winner = max(int(d['votes']) for d in candidates.values())
for name, value in candidates.items():
    if candidates.get(name, {}).get("votes") == winner:
        winner_name = name
        print(f"Winner: {name}")
    else:
        pass

# Output to file
output_path = os.path.join("Output", "election_results.csv")

# Open the file using "write" mode and specify the variable
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the Title and Total Votes
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['Total Votes',total_votes])

    # Write column headers
    csvwriter.writerow(['Candidate', 'Percent of Votes', 'Total Votes'])

    # Write results
    for key, value in candidates.items():
        csvwriter.writerow([key,str(value['percent_votes']) + "%",value['votes']])
    
    # Write winner
    csvwriter.writerow(['Winner', winner_name])









