#import libraries needed to scrape 538.com
import requests
import csv
from bs4 import BeautifulSoup as bs

#create a BeautifulSoup object for the NFL Games page 
prefix = "https://projects.fivethirtyeight.com/2022-nfl-predictions/games/"
webpage_response = requests.get(prefix)
webpage=webpage_response.content
soup = bs(webpage, "html.parser")

#separate out each week, then each game.  Save the games into a dictionary keyed by week. 
week=soup.select('.h3')
game=soup.select('.game-body')
game_weeks={}
for section in soup.find_all('section', class_='week'):
    game_weeks[section.h3.get_text()]=[]
    playing_games=section.find_all('table', class_='game-body')
    for each in playing_games:
        teams=each.find_all('td', class_='td text team')
        spreads=each.find_all('td', class_='td number spread')
        try:            game_weeks[section.h3.get_text()].append([teams[0].get_text(),spreads[0].get_text(),teams[1].get_text(),spreads[1].get_text()])
        except:
            continue


#The website only provides one spread per game (i.e., '-3.5').  This nested loop iterates through each game and adds the missing point spread. 
for keys,values in game_weeks.items():
    if(isinstance(values, list)):
        for value in values:
            if value[1]=='':
                try:
                    value[3]=float(value[3]) #convert spread string to float
                    value[1]=abs(value[3])
                except:
                    value[3]=0
                    value[1]=value[3]
            elif value[3]=='':
                try:
                    value[1]=float(value[1]) #convert spread string to float
                    value[3]=abs(value[1])
                except:
                    value[1]=0
                    value[3]=value[1]
            #if (value[1] or value[3] == 'PK'):
            #    value[1]=0
            #    value[3]=0
                    
#game_weeks is a dicitonary of the games of the week.  For export, we want a new dicitonary: key=week, values=team,spread.  Similar, just separating teams out of their games.
team_spreads_weekly={}
for keys,values in game_weeks.items():
    for value in values:
        if keys in team_spreads_weekly:
            team_spreads_weekly[keys].append([value[0],value[1]])
            team_spreads_weekly[keys].append([value[2],value[3]])
        else:
            team_spreads_weekly[keys]=[[value[0],value[1]]]
            team_spreads_weekly[keys].append([value[2],value[3]])

#grouping spreads by team, rather than by week.
weekly_spreads_per_team={'49ers': [],
                        'Bears': [],
                        'Bengals':[],
                        'Bills':[],
                        'Broncos':[],
                        'Browns':[],
                        'Buccaneers':[],
                        'Cardinals':[],
                        'Chargers':[],
                        'Chiefs':[],
                        'Colts':[],
                        'Cowboys':[],
                        'Dolphins':[],
                        'Eagles':[],
                        'Falcons':[],
                        'Giants':[],
                        'Jaguars':[],
                        'Jets':[],
                        'Lions':[],
                        'Packers':[],
                        'Panthers':[],
                        'Patriots':[],
                        'Raiders':[],
                        'Rams':[],
                        'Ravens':[],
                        'Saints':[],
                        'Seahawks':[],
                        'Steelers':[],
                        'Texans':[],
                        'Titans':[],
                        'Vikings':[],
                        'Washington':[],
                        }

fields=['teams'] 
for key in team_spreads_weekly.keys():  #begins nested loops to populate team_spreads_weekly with team scores in remaining weeks.
    fields.append(key) #<---formats out headers for the output
    playing_teams=[] #list of teams playing in a given week. 
    for i in range(0,len(team_spreads_weekly[key])):
        playing_teams.append(team_spreads_weekly[key][i][0])  #builds temporary list
    for key2 in weekly_spreads_per_team.keys(): # compares against the temporary list.  If missing, populates 'bye' week. 999=bye
        if key2 not in playing_teams:
            weekly_spreads_per_team[key2].append(999)
    for value in team_spreads_weekly[key]: #with bye weeks solved, populates the rest of the teams' scores for the week. 
        weekly_spreads_per_team[value[0]].append(value[1])
#print(weekly_spreads_per_team)



with open('output.csv','w') as output:
    log_writer=csv.writer(output)
    #log_writer.writeheader()
    log_writer.writerow(fields)
    for item in weekly_spreads_per_team:
        line=[item]
        for n in weekly_spreads_per_team[item]:
            line.append(n) 
        log_writer.writerow(line)












