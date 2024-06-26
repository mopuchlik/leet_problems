# Given an integer array nums of unique elements, return all possible
# subsets (the power set).

# The solution set must not contain duplicate subsets.
# Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# %%

from itertools import chain, combinations

# %%

# # itertools version
# def subsets(s):

#     res = chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
#     res = [list(ele) for ele in res]

#     return res


# https://leetcode.com/problems/subsets/solutions/5088950/video-we-have-two-choices-for-each-number/
def subsets(nums):
    res = []
    subset = []

    def create_subset(i):
        if i == len(nums):
            res.append(subset[:])
            print(res)
            return

        subset.append(nums[i])
        # print(subset)
        create_subset(i + 1)

        subset.pop()
        # print(subset)
        create_subset(i + 1)

    create_subset(0)
    return res


# %%
nums = [1, 2, 3]
a = subsets(nums)
# %%
