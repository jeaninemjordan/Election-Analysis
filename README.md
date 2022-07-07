# Election-Analysis
## An audit of Colorado electoral data utilzing Python.

Below is a screenshot of the text document produced when the election audit script in the PyPoll_Challenge.py code is ran. All data listed above is visible in an easy to read, easy to understand list for the viewer. 

INSERT SCREENSHOT OF TXT FILE RESULTS HERE

The dataset this audit utilizes is stored within a CSV file listing the Ballot ID, County and Candidate Voted For in columns (The election_results.csv file located within the Resources folder). The Python script written reads and analyzes this dataset, outputting the desired information into a text file for optimal viewing. The script defines the candidate names as a list, creates a dictionary where the candidates’ names are stored as keys, and reports the number of votes as values. This same coding is used to report the county voter turnout data as well.  


When the election audit was expanded to include the voter turnout by county, the viewer was given a better understanding of the poll to conduct further analysis with. This data could be useful in many ways to help forecast, study demographics, as well as plan future campaigns and elections. 


Updating the script to include county data was a minor adjustment that helped produce more meaningful results within the analysis. Additional updates could be made to this code that further analyze the county turnout data using the provided dataset. For instance, an additional if-statement could be used to analyze the candidate votes by county to determine the percentage share each candidate had in each of the recorded counties. This would allow us to view the winning candidate conclusions by county.  

This script could be expanded to include as many results as the data given provided it with to analyze. Using for loops and nested for loops, county turnout, city turnout, voting party, or any other further demographical statistics could be calculated if the dataset provided this additional information. Furthermore, the script could also be edited to be used on a state level or expanded to include as many candidates and counties as necessary for a larger analysis.  
