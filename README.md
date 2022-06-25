# Election_Analysis
Election analysis utilizing python coding

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidata won.
5. Determine the winner of the election based on popular vote.

### Update Overview
The Elections commision has requested additional data be provided in the analysis above. For a complete audit they would like to include the voter turnout for each county, the percentage of votes from each base on total votes, and the county with the highest voter turnout. 

#### Continued from previous list
6. Get a complete list of counties within the election_reults.csv.
7. Calculate the total number of votes within each county
8. Calculate the percentage of votes for each county.
9. Determine the county with the largest voter turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7, Visual Studio Code, 1.68.1

## Election Results Output
The final analysis of the election shows that:
- There are "x" votes cast in the election.
- The counties and their individual results were:
  - County 1 contained "x%" of the vote and "y" number of votes.
  - County 2 contained "x%" of the vote and "y" number of votes.
  - County 3 contained "x%" of the vote and "y" number of votes.
- The county with the largest voter turnout of the election was:
  - County (1, 2, or 3)
- The candidates and their individual results were:
  - Candidate 1 recieved "x%" of the vote and "y" number of votes.
  - Candidate 2 recieved "x%" of the vote and "y" number of votes.
  - Candidate 3 recieved "x%" of the vote and "y" number of votes.
- The winner of the election was:
  - Candidate (1, 2, or 3), who received "x%" of the vote and "y" number of votes.

![](Resources/Election_results_output.png | width="100")

## Summary
With some minor changes the provided script could be utilized for any election. Below you will find a two optional features that could faciltate this update:
- The addition of selecting your input and output file names and locations through a GUI rather than a preset of hardcoded file names and locations.
- Utilize the header record to determine index of specific field names
