def form_p2(regex, sub_data_players_stats, player_actions, player_name):
    p2 = regex.search(player_actions)

    try:
        if (p2.group(1) == player_name):
            sub_data_players_stats['2P'] += 1
            sub_data_players_stats['2PA'] += 1
            sub_data_players_stats['FG'] += 1
            sub_data_players_stats['FGA'] += 1
            sub_data_players_stats['PTS'] += 2

    except:
        pass


def form_p2a(regex, sub_data_players_stats, player_actions, player_name):

    p2a = regex.search(player_actions)

    try:
        if p2a.group(1) == player_name:
            sub_data_players_stats['2PA'] += 1
            sub_data_players_stats['FGA'] += 1

    except:
        pass


def form_p3(regex, sub_data_players_stats, player_actions, player_name):

    p3 = regex.search(player_actions)

    try:
        if p3.group(1) == player_name:
            sub_data_players_stats['3P'] += 1
            sub_data_players_stats['3PA'] += 1
            sub_data_players_stats['FG'] += 1
            sub_data_players_stats['FGA'] += 1
            sub_data_players_stats['PTS'] += 3
    except:
        pass


def form_p3a(regex, sub_data_players_stats, player_actions, player_name):

    p3a = regex.search(player_actions)

    try:
        if p3a.group(1) == player_name:
            sub_data_players_stats['3PA'] += 1
            sub_data_players_stats['FGA'] += 1

    except:
        pass


def form_orb(regex, sub_data_players_stats, player_actions, player_name):
    orb = regex.search(player_actions)

    try:
        if orb.group(1) == player_name:
            sub_data_players_stats['ORB'] += 1

    except:
        pass


def form_drb(regex, sub_data_players_stats, player_actions, player_name):
    drb = regex.search(player_actions)

    try:
        if drb.group(1) == player_name:
            sub_data_players_stats['DRB'] += 1

    except:
        pass


def form_ft(regex, sub_data_players_stats, player_actions, player_name):
    ft = regex.search(player_actions)

    try:
        if ft.group(1) == player_name:
            sub_data_players_stats['FT'] += 1
            sub_data_players_stats['FTA'] += 1
            sub_data_players_stats['PTS'] += 1

    except:
        pass


def form_fta(regex, sub_data_players_stats, player_actions, player_name):
    fta = regex.search(player_actions)

    try:
        if fta.group(1) == player_name:
            sub_data_players_stats['FTA'] += 1

    except:
        pass


def form_cft(regex, sub_data_players_stats, player_actions, player_name):
    cft = regex.search(player_actions)

    try:
        if cft.group(1) == player_name:
            sub_data_players_stats['FT'] += 1
            sub_data_players_stats['FTA'] += 1
            sub_data_players_stats['PTS'] += 1
            sub_data_players_stats['CFT'] += 1

    except:
        pass


def form_ast(regex, sub_data_players_stats, player_actions, player_name):
    ast = regex.search(player_actions)

    try:
        if ast.group(1) == player_name:
            sub_data_players_stats['AST'] += 1

    except:
        pass


def form_stl(regex, sub_data_players_stats, player_actions, player_name):
    stl = regex.search(player_actions)

    try:
        if stl.group(1) == player_name:
            sub_data_players_stats['STL'] += 1
    except:
        pass


def form_blk(regex, sub_data_players_stats, player_actions, player_name):
    blk = regex.search(player_actions)

    try:
        if blk.group(1) == player_name:
            sub_data_players_stats['BLK'] += 1

    except:
        pass


def form_tov(regex, sub_data_players_stats, player_actions, player_name):
    tov = regex.search(player_actions)

    try:
        if tov.group(1) == player_name:
            sub_data_players_stats['TOV'] += 1

    except:
        pass


def form_pf(regex, sub_data_players_stats, player_actions, player_name):
    pf = regex.search(player_actions)

    try:
        if pf.group(1) == player_name:
            sub_data_players_stats['PF'] += 1

    except:
        pass



