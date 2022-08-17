# FiveThirtyEightScrape
Scrapes the games for the rest of the year off of 538, with spreads per team.

My goal for this repo was to make it easier to calculate the smartest move for a given week in Survival football leagues.  Rather than going to FiveThirtyEight and manually deciding which team to take this week, I let the algorithm decide the best choices. 

1. Script.py reads the game predictions off of FiveThirtyEight's NFL probability page, populates the missing predictions from each game, and sorts the data into a .csv in alphabetical order.
2. Use Excel's data function to import the .csv into "MK_Survival" and override the existing list of teams. 
3. Delete any team rows that you've already picked this year. 
4. The Solver equation really does the heavy lifting here.  It will attempt to minimize the overall score by picking two teams per week and adding the overall FiveThirtyEight probability. 
