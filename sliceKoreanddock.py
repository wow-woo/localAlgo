# TODO: I will come back and resolve this.
# n : number of ddocks in stock.
# m : number of requested length of ddock.
# h : length from end of most long ddock to the point to cut.
# you need to slice ddock by h at less. as long as sum of sliced ddock is longer than m.

n = 4
m = 6
ddocks = [19, 15, 10, 17]

# sort ddocks to find out most long ddock
longest_ddock = sorted(ddocks, reverse=True)[0]


def get_minimum_h(ddocks, n, m, least_cut, most_cut, candidates):
    if least_cut > most_cut:
        return max(candidates)

    # the adjustment length
    mid_cut = (least_cut+most_cut) // 2

    # get sum.
    sum = 0
    for ddock in ddocks:
        min_len_to_cut = most_cut-mid_cut

        if ddock > min_len_to_cut:
            sum += (ddock-min_len_to_cut)

    if sum == m:
        return mid_cut
    elif sum > m:
        candidates.append(mid_cut)
        return get_minimum_h(ddocks, n, m, least_cut, mid_cut - 1, candidates)
    elif sum < m:
        return get_minimum_h(ddocks, n, m, mid_cut+1, most_cut, candidates)


result = get_minimum_h(ddocks, n, m, 0, longest_ddock, [])
print(result)
# i screwed it up, because i was confused with all the lengths.
