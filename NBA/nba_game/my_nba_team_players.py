import re

with open('nba_game_warriors_thunder_20181016.txt') as nba_data:
    nba_data = [nba.split('|') for nba in nba_data.read().split('\n')[0:-1]]


def data_players_match(all_players_names):

    team_player = {name: '' for name in all_players_names}

    p2_form = re.compile(r'([^\s]+\. [A-Z]\w*) makes 2-pt', re.I)
    orb_form = re.compile(r'Offensive rebound by ([^\s]+\. [A-Z]\w*)', re.I)
    drb_form = re.compile(r'Defensive rebound by ([^\s]+\. [A-Z]\w*)', re.I)
    p3a_form = re.compile(r'([^\s]+\. [A-Z]\w*) misses 3-pt', re.I)

    for event in nba_data:
        p2 = p2_form.search(event[-1])

        try:
            name = p2[1]
            team_player[name] = event[2]
        except:
            pass
        orb = orb_form.search(event[-1])

        try:
            name = orb[1]
            team_player[name] = event[2]
        except:
            pass

        drb = drb_form.search(event[-1])

        try:
            name = drb[1]
            team_player[name] = event[2]
        except:
            pass

        p3a = p3a_form.search(event[-1])

        try:
            name = p3a[1]
            team_player[name] = event[2]
        except:
            pass

    return team_player
