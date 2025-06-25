# Given an integer array nums and an integer val, remove all occurrences
# of val in nums in-place. The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k,
# to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5


def remove_elts(nums, val):

    n_nums = len(nums)

    k = 0
    while True:
        for i, num_i in enumerate(nums):
            if i == n_nums - k:
                return n_nums - k
            if num_i != val:
                continue
            else:
                nums[i : n_nums - 1 - k] = nums[i + 1 : n_nums - k]
                nums[n_nums - 1 - k] = val
                k += 1
                break


# nums = [3, 2, 2, 3]
# val = 3
# print(remove_elts(nums, val))


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(remove_elts(nums, val))
