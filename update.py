
def update_dict(rev_rank, rev_name, rev_time):

    player_list = []

    i = 0
    for rank in rev_rank:
        rank_list = []
        
        rank_list.append(rev_name[i])
        rank_list.append(rev_time[i])
        
        player_list.append(rank_list)

        i += 1

    return player_list