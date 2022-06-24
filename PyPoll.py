#import dependences
import csv
import os

# In this project, our final Python script will need to be able to deliver the following information when the script is run: 
#   - Total number of votes cast
#   - A complete list of candidates who received votes
#   - Total number of votes each candidate received
#   - Percentage of votes each candidate won
#   - The winner of the election based on popular vote

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Open the data file.
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

# 2. Write down the names of all the candidates.
# Using the with statement open the file as a text file.
    with open(file_to_save, "w") as txt_file:

        # Write some data to the file.
        txt_file.write("Counties in the Election\n-------------------------\n")
        # Write three counties to the file.
        txt_file.write("Arapahoe\nDenver\nJefferson")

# 3. Add a vote count for each candidate.

# 4. Get the total votes for each candidate.

# 5. Get the total votes cast for the election.

# Close the file.
#election_data.close()