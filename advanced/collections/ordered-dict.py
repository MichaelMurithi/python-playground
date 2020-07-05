# Demonstrate the usage of OrderedDict objects

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    # TODO: create an ordered dictionary of the teams
    teams = OrderedDict(sortedTeams)
    # TODO: Use popitem to remove the top item
    teamName, wins_loses = teams.popitem(False) #pops a value from the start of the dictionary
    print('The top team is:', teamName, wins_loses)
    # TODO: What are next the top 4 teams?
    print('The other four teams are')
    for i,team in enumerate(teams, start=1):
        print(i, team)
       
    # TODO: test for equality

if __name__ == "__main__":
    main()
