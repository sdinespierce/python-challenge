#import dependencies
import os
import csv

#read in csv
py_poll_csv = os.path.join("Resources", "election_data.csv")

#initialize variables
vote_count = 0
name_list = []
num_of_votes_list = []
output = ""
candidate_output = ""

#open file
with open(py_poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #loop rows in csv
    for row in csvreader:
        #count rows
        vote_count += 1
        #define local var
        candidate_name = row[2]

        #check to see if candidate name has been voted for before
        if candidate_name in name_list:
            #if yes, increment vote count
            index = name_list.index(candidate_name)
            num_of_votes_list[index] += 1
        else:
            #if no, make a new entry then increment
            name_list.append(candidate_name)
            index = name_list.index(candidate_name)
            num_of_votes_list.append(0)
            num_of_votes_list[index] += 1

#loop name list and add lines to output
for i in range(len(name_list)):
    candidate_output += f"{(name_list[i])}: {round(100 * num_of_votes_list[i] / vote_count, 2)}% ({num_of_votes_list[i]})\n"

#output
output = "Election Results \n" 
output += "-------------------------" + "\n"
output += "Total Votes: " + str(vote_count) + "\n" 
output += "-------------------------" + "\n"
output += candidate_output
output += "-------------------------" + "\n"
output += "Winner: " + name_list[num_of_votes_list.index(max(num_of_votes_list))] + "\n"
output += "-------------------------"

print (output)

#writes output to txt file
output_file = os.path.join("analysis", "results.txt")
with open(output_file, "w") as datafile:
    datafile.write(output)