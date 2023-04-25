from all_functions import *

all_players_names = data_players_name(nba_data)
data_players_stat = data_players_stats(nba_data, all_players_names)


def warriors(data_players_stat, *team):
    total_col = {"Team Totals": 'Team Totals', "FG": 0, "FGA": 0, "FG%": 0.0, "3P": 0, "3PA": 0, "3P%": 0.0, "FT": 0,
                 "FTA": 0, "FT%": 0.0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}

    headers = [k for k in data_players_stat[0].keys()]

    print('\nGOLDEN_STATE_WARRIORS\n')
    print(*headers, sep='  ')
    for play in data_players_stat:
        if(play['player_name'] in team[0]):

            total_col['FG'] += play['FG']
            total_col['FGA'] += play['FGA']
            total_col['3P'] += play['3P']
            total_col['3PA'] += play['3PA']
            total_col['FT'] += play['FT']
            total_col['FTA'] += play['FTA']
            total_col['ORB'] += play['ORB']
            total_col['DRB'] += play['DRB']
            total_col['AST'] += play['AST']
            total_col['STL'] += play['STL']
            total_col['BLK'] += play['BLK']
            total_col['TOV'] += play['TOV']
            total_col['PF'] += play['PF']
            total_col['PTS'] += play['PTS']

            print(*play.values(), sep='  ')

    total_col['FG%'] = round(total_col['FG'] / total_col['FGA'], 3)
    total_col['3P%'] = round(total_col['3P'] / total_col['3PA'], 3)
    total_col['FT%'] = round(total_col['FT'] / total_col['FTA'], 3)
    total_col['TRB'] = total_col['ORB'] + total_col['DRB']

    print(*total_col.values(), sep=' ')
