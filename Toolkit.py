def get_pairs(list0):
    pairs = {}
    for i in range(0, len(list0)//2+2, 2):
        pairs[list0[i]] = list0[i+1]
    return pairs
