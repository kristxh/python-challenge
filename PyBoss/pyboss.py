import os
import csv
import json

#Path to collect data from the Resources folder
file_path = os.path.join("Resources", "employee_data.csv")
states_file_path = os.path.join("Resources", "us_state_abbreviations.json")

#Global variables
rows = []
new_rows = []
states = {}

#Import the employee_data.csv file into the rows list
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    rows = []
    for i, row in enumerate(csvreader):
        if i==0:
            header = row
        else:
            rows.append(row)

#Import the states json file into a dictionary
with open(states_file_path,'r') as json_file:
    states = json.load(json_file)

#Loop through the rows list, split first and last name, create a new list 
for row in rows:
    first_name, last_name = row[1].split(' ')
    masked_ssn = ("***-**-" + row[3][7:])
    date_list = row[2].split('-')
    new_date = "{}/{}/{}".format(date_list[1],date_list[2],date_list[0]) 
    state_abbr = states.get(row[4])
    new_rows_list= [row[0],first_name,last_name,new_date,masked_ssn,state_abbr]
    new_rows.append(new_rows_list)

#Output to file
output_path = os.path.join("Output", "employee_analysis.csv")

#Open the file using "write" mode and specify the variable
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the column titles
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    
    # Write the values
    for row in new_rows:
        csvwriter.writerow(row)
