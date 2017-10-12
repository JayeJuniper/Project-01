
import csv

def reader_sort():
# read the data from the supplied CSV file. 
# Stores player data as dictionaries in two lists, one for players with experienced and one without
    exp_list = []
    noexp_list = []
    with open('soccer_players.csv', newline='') as csvfile:   
    #compose lines as dicts          
        roster_reader = csv.DictReader(csvfile, delimiter=',')     
        # make two lists; one of players with experience and one without        
        for row in roster_reader:     
            if row['Soccer Experience'] == 'YES':
                exp_list.append(row) 
            else:
                noexp_list.append(row)
        team_builder(exp_list, noexp_list) 

    
def team_builder(exp_list, noexp_list):
# Create logic that can iterate through all 18 players and assign them to teams such that each team has the same number of players. The number of experienced players on each team should also be the same.
    sharks = []
    dragons = []
    raptors = []
    
    #places three experienced players in each team (as dictionaries)
    for player in exp_list[:3]:
        sharks.append(player)
    for player in exp_list[3:6]:
        dragons.append(player)
    for player in exp_list[6:]:
        raptors.append(player)

    #places three players without experience in each team (as dictionaries)
    for player in noexp_list[:3]:
        sharks.append(player)
    for player in noexp_list[3:6]:
        dragons.append(player)
    for player in noexp_list[6:]:
        raptors.append(player)
    format_export(sharks, dragons, raptors) 


def format_export(sharks, dragons, raptors):
# format and export in -- teams.txt -- 
# team name followed by each player name, whether they've played soccer before and their guardians' names.
    with open("teams.txt", 'w') as file: 
        # write a string to the file
        file.write("Sharks:\n")
        for d in sharks:        #iterate through dictionary, separating needed components into list and writing to file (was having issues making more compact)
            player = d["Name"]
            exp = d["Soccer Experience"]
            guardians = d["Guardian Name(s)"]
            temp = [player, exp, guardians]
            file.write(", ".join(temp)+'\n')
        file.write("\nDragons:\n")    
        for d in dragons:
            player = d["Name"]
            exp = d["Soccer Experience"]
            guardians = d["Guardian Name(s)"]
            temp = [player, exp, guardians]
            file.write(", ".join(temp)+'\n')
        file.write("\nRaptors:\n")
        for d in raptors:
            player = d["Name"]
            exp = d["Soccer Experience"]
            guardians = d["Guardian Name(s)"]
            temp = [player, exp, guardians]
            file.write(", ".join(temp)+'\n')
            

if __name__ == "__main__":        
    reader_sort()
