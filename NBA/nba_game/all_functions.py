from my_nba_team_players import data_players_match
from my_nba_game_functions import *
import re

global nba_data


with open('nba_game_warriors_thunder_20181016.txt') as nba_data:
    nba_data = [nba.split('|') for nba in nba_data.read().split('\n')[0:-1]]


def data_players_name(nba_data):
    form_name = re.compile(r'([^\s]+\. [A-Z]\w*)', re.I)

    all_players = []

    for row in nba_data:
        name = form_name.search(row[-1])
        if name:
            all_players.append(name.group(0))

    return list(set(all_players))


def data_players_stats(nba_data, all_players_names):

    list_of_all_player_stats = []

    for player_name in all_players_names:

        sub_data_players_stats = {"player_name": '', "2P": 0, "2PA": 0, "FG": 0, "FGA": 0, "FG%": 0.0, "3P": 0, "3PA": 0, "3P%": 0.0,
                                  "FT": 0, "CFT": 0, "FTA": 0, "FT%": 0.0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}

        for player_actions in nba_data:
            sub_data_players_stats['player_name'] = player_name

            form_p2(re.compile(r'([^\s]+\. [A-Z]\w*) makes 2-pt', re.I),
                    sub_data_players_stats, player_actions[-1], player_name)

            form_p2a(re.compile(r'([^\s]+\. [A-Z]\w*) misses 2-pt', re.I),
                     sub_data_players_stats, player_actions[-1], player_name)

            form_p3(re.compile(r'([^\s]+\. [A-Z]\w*) makes 3-pt', re.I),
                    sub_data_players_stats, player_actions[-1], player_name)

            form_p3a(re.compile(r'([^\s]+\. [A-Z]\w*) misses 3-pt', re.I),
                     sub_data_players_stats, player_actions[-1], player_name)

            form_orb(re.compile(r'Offensive rebound by ([^\s]+\. [A-Z]\w*)', re.I),
                     sub_data_players_stats, player_actions[-1], player_name)

            form_drb(re.compile(r'Defensive rebound by ([^\s]+\. [A-Z]\w*)', re.I),
                     sub_data_players_stats, player_actions[-1], player_name)

            form_ft(re.compile(r'([^\s]+\. [A-Z]\w*) makes free throw', re.I),
                    sub_data_players_stats, player_actions[-1], player_name)

            form_fta(re.compile(r'([^\s]+\. [A-Z]\w*) misses free throw', re.I),
                     sub_data_players_stats, player_actions[-1], player_name)

            form_cft(re.compile(r'([^\s]+\. [A-Z]\w*) makes clear path free throw',
                     re.I), sub_data_players_stats, player_actions[-1], player_name)

            form_ast(re.compile(r'assist by ([^\s]+\. [A-Z]\w*)', re.I),
                     sub_data_players_stats, player_actions[-1], player_name)

            form_stl(re.compile(r'steal by ([^\s]+\. [A-Z]\w*)', re.I),
                     sub_data_players_stats, player_actions[-1], player_name)

            form_blk(re.compile(r'block by ([^\s]+\. [A-Z]\w*)', re.I),
                     sub_data_players_stats, player_actions[-1], player_name)

            form_tov(re.compile(r'Turnover by ([^\s]+\. [A-Z]\w*)', re.I),
                     sub_data_players_stats, player_actions[-1], player_name)

            form_pf(re.compile(r'foul by ([^\s]+\. [A-Z]\w*)', re.I),
                    sub_data_players_stats, player_actions[-1], player_name)

        list_of_all_player_stats.append(sub_data_players_stats)

    for el in list_of_all_player_stats:
        try:
            el['FG%'] = round(el['FG'] / el['FGA'], 3)
            el['3P%'] = round(el['3P'] / el['3PA'], 3)
            el['FT%'] = round(el['FT'] / el['FTA'], 3)
            el['TRB'] = el['ORB'] + el['DRB']
        except:
            pass

    # for a in list_of_all_player_stats:
    #     print(a.values())

    for del_el in list_of_all_player_stats:
        del del_el['CFT']
        del del_el['2P']
        del del_el['2PA']

    return list_of_all_player_stats
