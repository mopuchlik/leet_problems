# Given a non-empty array of integers nums, every element
# appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity
# and use only constant extra space.

# Example 1:

# Input: nums = [2,2,1]
# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:

# Input: nums = [1]
# Output: 1


# %%
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) == 1:
        return nums[0]

    nums.sort()

    for i in range(0, len(nums) - 1, 2):
        if nums[i] == nums[i + 1]:
            if i == len(nums) - 3:
                return nums[len(nums) - 1]
            else:
                pass
        else:
            return nums[i]


# %%

nums = [2, 2, 1]
nums = [4, 1, 4, 1, 2]
nums = [1]
nums = [
    -336,
    513,
    -560,
    -481,
    -174,
    101,
    -997,
    40,
    -527,
    -784,
    -283,
    -336,
    513,
    -560,
    -481,
    -174,
    101,
    -997,
    40,
    -527,
    -784,
    -283,
    354,
]
res = singleNumber(nums)
print(res)

# %%
