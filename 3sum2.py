# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
# Notice that the order of the output and the order of the triplets does not matter.

# Example 1
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


def threeSum(nums):

    result = []

    # sort
    nums.sort()

    n_nums = len(nums)
    for i in range(n_nums):
        for j in range(n_nums):
            k = i + 1
            while i < k and k < j:
                if nums[i] + nums[k] + nums[j] == 0:
                    res_i = [nums[i], nums[k], nums[j]]
                    res_i.sort()
                    if res_i not in result:
                        result.append(res_i)
                k += 1

    return result


nums = [-1, 0, 1, 2, -1, -4]
x = threeSum(nums)
print(x)
# Output: [[-1,-1,2],[-1,0,1]]

nums = [0, 1, 1]
x = threeSum(nums)
print(x)
# Output: []

nums = [0, 0, 0]
x = threeSum(nums)
print(x)
# Output: [0, 0, 0]
