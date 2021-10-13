def clean_data(date, ranks, names, times):

    revised_rank = []
    revised_name = []
    revised_time = []

    i = 0
    for rank in ranks:
        if len(rank) == 0:
            revised_rank.append(ranks[i - 1][0])
        else:
            revised_rank.append(rank[0])
        i += 1

    for name in names:
        revised_name.append(name[0])

    for time in times:
        revised_time.append(time[0])

    return revised_rank, revised_name, revised_time
