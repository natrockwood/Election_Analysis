import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save a file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Initialize list of candidates
candidate_options =[]
# Initialize dictionary of candidate votes
candidate_votes = {}
# Determine winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Initialize county list
counties = []
# Initialize dictionary of counties and votes
county_votes = {}
# Create empty string holding county name with largest turnout and winning county tracker for counties
county_mostvotes = ""
county_win_ct = 0
county_win_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Print the the header row.
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:
    # Add to the total vote count total_votes
        total_votes += 1

        # Print candidate name from each row
        candidate_name = row[2]
        # Print county name from each row
        county = row[1]
        
        # Add candidate names to the candidate list, if the candidate does not match any existing candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
        
            # Start tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add votes to the count
        candidate_votes[candidate_name] += 1

        # Add county name to counties list
        if county not in counties:
            counties.append(county)
    # print(counties)

            # Start tracking the county's vote count
            county_votes[county] = 0
        
        # Add votes to the county vote count
        county_votes[county] += 1
    # print(county_votes)

# Save results to text file
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Print out the voter turnout results
    for county in county_votes:
        # Retrieve county vote count
        cvotes = county_votes[county]
        # Calculate the % of votes per county
        vote_percentage = float(cvotes)/float(total_votes)*100

        county_results = (f"{county}: {vote_percentage:.1f}% ({cvotes:,})\n")

        print(county_results)
        txt_file.write(county_results)

        # Determine the winning county by using the vote count
        if (cvotes > winning_count) and (vote_percentage > county_win_percentage):
            county_win_ct = cvotes
            county_win_percentage = vote_percentage
            county_mostvotes = county   

    # Print out county with most votes
    largest_county_turnout = (
        f"-------------------------\n"
        f"Largest County Turnout: {county_mostvotes}\n"
        f"-------------------------\n")
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)

    # Determine the % of votes for each candidate by looping through the counts & iterate through the cadidate list
    for candidate in candidate_votes:
        # Retrieve cand vote count
        votes = candidate_votes[candidate] # from if statement above
        # Calculate the % of votes
        vote_percentage = float(votes)/float(total_votes)*100

        # Print out each candidate's name, vote count, and percentage of votes to the terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count and cand & determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true, set winning_count = votes & winning_percentage = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning_candidate to cand's name
            winning_candidate = candidate

    # Print out winning summary
    winning_cand_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_cand_summary)
    txt_file.write(winning_cand_summary)