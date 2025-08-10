# %%
# you have
# levels = List[num]
# maxSpread = num
# return min groups that contain numbers within a maxSpread


def groupDivision(levels, maxSpread):
    levels.sort()

    n_group = 1
    benchmark_val = levels[0]

    # print(levels_tmp)
    for i in range(1, len(levels)):
        if abs(levels[i] - benchmark_val) <= maxSpread:
            continue
        else:
            n_group += 1
            benchmark_val = levels[i]

    return n_group


# %%
levels = [1, 2, 3, 4, 5, 8, 10, 100]
maxSpread = 2

# %%
groupDivision(levels, maxSpread)
