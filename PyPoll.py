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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: perform analysis.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    # for row in file_reader:
    #    print(row)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    txt_file.write("Counties in Election\n-----------------------\n")
# Write three countries to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson") # \n = enter

# Close the file
txt_file.close()