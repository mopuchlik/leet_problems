# %%

strs = ["flower", "flow", "flight"]


# %%
def longest_pref(strs):

    strs = strs.copy()

    # calculate lengths to take min length
    lst_lengths = [len(strs[x]) for x in range(len(strs))]
    min_index = lst_lengths.index(min(lst_lengths))

    benchmark = strs[min_index]
    strs.pop(min_index)
    lst_to_compare = strs

    # main loop
    for i in range(len(benchmark)):
        lst_tmp = [lst_to_compare[k][i] for k in range(len(lst_to_compare))]
        if all([lst_tmp[k] == benchmark[i] for k in range(len(lst_tmp))]):
            i += 1 
            continue
        else: 
            break

    result = benchmark[:i]

    return result

#%%
longest_pref(strs)


# print(longest_pref(strs))

#%%



