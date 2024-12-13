# %%

strs = ["flower", "flow", "flight"]


# %%
def longest_pref(strs):

    for k in range(len(strs)):

        list_trim = []
        for i in range(len(strs)):
            list_trim.append(strs[i][k])

        print(list_trim)
        check = all(list_trim[0][0] in string for string in list_trim)
        if check:
            common_pref = strs[0][0 : k + 1]
            # print(k)

        else:
            break
    return common_pref


print(longest_pref(strs))
