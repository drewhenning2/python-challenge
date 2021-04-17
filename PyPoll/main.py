# import modules
import os
import csv

# change directories
py_poll_csv = os.path.join("Resources", "election_data.csv")

# open csv file in read mode
with open(py_poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
# skip the header row 
    next(csvreader)

# count total number of votes cast
    total_votes_cast = []

    for row in csvreader:
        total_votes_cast.append(row[2])

# calculate percentage and total votes for Khan
    khan_count = "Khan"
    khan_total_votes = total_votes_cast.count(khan_count)
    khan_percentage = khan_total_votes/len(total_votes_cast)
    k_percent = "{:.3%}".format(khan_percentage)

# calculate percentage and total votes for Correy
    correy_count = "Correy"
    correy_total_votes = total_votes_cast.count(correy_count)
    correy_percentage = correy_total_votes/len(total_votes_cast)
    c_percent = "{:.3%}".format(correy_percentage)

# calculate percentage and total votes for Li
    li_count = "Li"
    li_total_votes = total_votes_cast.count(li_count)
    li_percentage = li_total_votes/len(total_votes_cast)
    l_percent = "{:.3%}".format(li_percentage)

# calculate percentage and total votes for O'Tooley    
    otooley_count = "O'Tooley"
    otooley_total_votes = total_votes_cast.count(otooley_count)
    otooley_percentage = otooley_total_votes/len(total_votes_cast)
    o_percent = "{:.3%}".format(otooley_percentage)

# calculate winner with the most votes
    if khan_total_votes > max(correy_total_votes, li_total_votes, otooley_total_votes):
        winning_candidate = "Khan"
    elif correy_total_votes > max(khan_total_votes, li_total_votes, otooley_total_votes):
        winning_candidate = "Correy"
    elif li_total_votes > max(khan_total_votes, correy_total_votes, otooley_total_votes):
        winning_candidate = "Li"
    else:
        winning_candidate = "O'Tooley"



# calculate total votes casted
    total_votes_cast = len(total_votes_cast)

# print to terminal
print(f'''
Election Results
------------------------
Total Votes: {total_votes_cast}
------------------------
Khan: {k_percent} ({khan_total_votes})
Correy: {c_percent} ({correy_total_votes})
Li: {l_percent} ({li_total_votes})
O'Tooley: {o_percent} ({otooley_total_votes})
------------------------
Winner: {winning_candidate}
------------------------
''')

# export to txt file
output_file_path = os.path.join("Analysis", 'election_results.txt')
with open(output_file_path, 'w') as output_file:

    output_file.write("Election Results")
    output_file.write("\n")

    output_file.write("------------------------")
    output_file.write("\n")

    output_file.write(f"Total Votes: {total_votes_cast}")
    output_file.write("\n")

    output_file.write(f"Khan: {k_percent} ({khan_total_votes})")
    output_file.write("\n")

    output_file.write(f"Correy: {c_percent} ({correy_total_votes})")
    output_file.write("\n")

    output_file.write(f"Li: {l_percent} ({li_total_votes})")
    output_file.write("\n")

    output_file.write(f"O'Tooley: {o_percent} ({otooley_total_votes})")
    output_file.write("\n")

    output_file.write("------------------------")
    output_file.write("\n")

    output_file.write(f"Winner: {winning_candidate}")
    output_file.write("\n")

    output_file.write("------------------------")