from all_functions import *
from okhlahoma import okhlahoma
from warriors import warriors


def print_data(data_players_stat, *team):

    warriors(data_players_stat, *team)
    okhlahoma(data_players_stat, *team)


def analyse_nba_game(play_by_play_moves):
    all_players_names = data_players_name(play_by_play_moves)
    data_players_stat = data_players_stats(
        play_by_play_moves, all_players_names)
    player_team = data_players_match(all_players_names)

    home_team = []
    away_team = []

    for el in player_team.keys():
        if player_team[el] == 'GOLDEN_STATE_WARRIORS':
            home_team.append(el)
        else:
            away_team.append(el)

    print_data(data_players_stat, home_team, away_team)


analyse_nba_game(nba_data)
