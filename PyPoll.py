# The data we need to retreive:
# •	Total number of votes cast
# •	A complete list of candidates who received votes
# •	Total number of votes each candidate received
# •	Percentage of votes each candidate won
# •	The winner of the election based on popular vote

# Add dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save a file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1.1 Initialize a total vote counter.
total_votes = 0
# 2.1 Initialize list of candidates
candidate_options =[]
# 3.1 Initialize dictionary of candidate votes
candidate_votes = {}
# 5.0 Determine winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Print the the header row.
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:
    # 1.2 Add to the total vote count total_votes
        total_votes += 1 # putting 'print(total_votes)' in the for loop will print each line of the files
        
        # 2.2 Print candidate name from each row
        candidate_name = row[2]
        
        # 2.3 Add candidate names to the candidate list, if the candidate does not match any existing candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
        
            # 3.2 Start tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        # 3.3 Add votes to the count
        candidate_votes[candidate_name] += 1

    # 4.0 Determine the % of votes for each candidate by looping through the counts
    # 4.1 Iterate through the cadidate list
    for candidate in candidate_votes:
        # 4.2 Retrieve cand vote count
        votes = candidate_votes[candidate] # from if statement above
        # 4.3 Calculate the % of votes
        vote_percentage = float(votes)/float(total_votes)*100

        # 4.4 Print the cand name and % votes
        # print(f"{candidate}: received {votes:,} and {vote_percentage:.2f}% of the votes.")
        # 5.4 print out each candidate's name, vote count, and percentage of votes to the terminal.
        print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # 5.2 Determine winning vote count and cand
        # 5.3 Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If TRUE, set winning_count = votes & winning_percentage = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning_candidate to cand's name
            winning_candidate = candidate

    # 5.5 print out winning summary
    winning_cand_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_cand_summary)

# 3.4 Print Candidate vote dictionary
# print(candidate_votes)

# 2.4 Print Candidate List
# print(candidate_options)
# 1.3 Print total votes
# print(total_votes)

# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file