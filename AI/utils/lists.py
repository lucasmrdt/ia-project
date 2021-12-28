def alldiff(l):
    return len(set(l)) == len(l)


def sublists(l, size):
    def get_at_idx(idx):
        return l[idx % len(l)]

    for i in range(len(l)):
        ll = []
        for j in range(size):
            ll.append(get_at_idx(i + j))
        yield ll
