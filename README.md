# FiveThirtyEightScrape
Scrapes NFL games for the rest of the year off of 538, with spreads per team.

My goal for this repo was to make it easier to calculate the smartest move for a given week in Survival football leagues.  Rather than manually deciding which team to pick this week, I let the algorithm decide the best choices. 

General Directions for use:

1. Run Script.py to read the game predictions off of FiveThirtyEight's NFL probability page, populates the missing predictions from each game, and sorts the data into output.csv in alphabetical order.
2. Use Excel's data function to import the .csv into "Single Pick Per Week" and override the existing list of teams. 
3. Delete any team rows that you've already picked this year from the spreadsheet as well as the Solver constraints.
4. Run the solver solution. This requires that the Solver add-on be installed. Solver really does the heavy lifting here.  It will attempt to minimize the overall score by picking two teams per week and adding the overall FiveThirtyEight probability. 

It is currently the off-season, so FiveThirtyEight isn't populated.  I'll update the attached example spreadsheet and output.csv when the season restarts.  As of right now, the version of the spreadsheet and output in the repo are a snapshot from week 14 last year.  
