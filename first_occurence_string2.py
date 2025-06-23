# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.


def strStr(haystack, needle):

    n_needle = len(needle)

    res = -1

    for i, _ in enumerate(haystack):
        if haystack[i : i + n_needle] == needle:
            res = i
            break

    return res


# %%
haystack = "baaabbb"
needle = "aaa"
print(strStr(haystack, needle))

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))
