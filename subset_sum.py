"""
Created on 11/19/2022

Author: @alexf314

The subset-sum problem:
Given an array of integers, nums, and an integer, target: Return a subset of numbers from the array (no repetitions) which add up to target.
"""

"""
Inputs:
- num: An array of integers, length at least one
- target: An integer

Returns:
- False if there doesn't exist a subset of integers (size at least one) in num which add up to target
- Otherwise, returns a set of tuple-pairs, where for each pair, the first element in the pair is a number in nums, and the second element is that number's index in num. Each index is distinct, and the sum of all of the first elements is target.
"""
def subset_sum(nums: list, target: int) -> set or bool:
    # memo_table[i][j] is the answer to subset_sum(nums[0:i+1], j+1)
    # 0 <= i < len(nums) and 0 <= j < target
    memo_table = [[False]*target for i in range(len(nums))]

    # Three possibilities for memo_table[i][j]:
    # - If memo_table[i-1][j] filled, fill memo_table[i][j] with same
    # -     (i.e., subset_sum(i, j) = subset_sum(i-1, j))
    # - If num[i] < j and memo_table[i-1][j - num[i]] filled, fill memo_table[i][j] with same, in addition to (num[i], i)
    # -     (i.e., subset_sum(i,j) = subset_sum(i-1, j-nums[i]) + (nums[i], i))
    # - If num[i] = j, fill memo_table[i][j] with (num[i], i)
    # -     (i.e., subset_sum(i, j) = (nums[i], i))

    # Extract min and max numbers
    min_num, max_num = min(nums), max(nums)

    # Check if target is in bounds
    if (target < min_num) or (target > max_num):
        return False

    # Normalize nums (fresh array)
    nums = [number - min_num for number in nums]

    # Base cases:
    # - i = 0, j = nums[i] --> subset_sum(i, j) = j
    # - i = 0, j not = nums[i] --> subset_sum(i, j) = False

    # For the first element (the number), make sure to normalize back!
    memo_table[0][nums[0]] = {(nums[0]+min_num, 0)}

    for i in range(1, len(nums)):
        # Topological order: subproblems for smaller i have been calculated
        for j in range(0, max_num-min_num):
            # subset_sum(i, j) = subset_sum(i-1, j) if the latter exists
            subproblem1 = memo_table[i - 1][j]
            if subproblem1:
                memo_table[i][j] = subproblem1

            # subset_sum(i, j) = {nums[i]} if it equals j
            if nums[i] == j:
                memo_table[i][j] = {(nums[i]+min_num, i)}

            # subset_sum(i, j) = subset_sum(i-1, j-nums[i]) U {nums[i]} if the latter subproblem exists
            if j - nums[i] >= 0:
                subproblem2 = memo_table[i - 1][j - nums[i]]
                if subproblem2:
                    new_elem = {(nums[i]+min_num, i)}
                    memo_table[i][j] = subproblem2.union(new_elem)

    # Remember, we normalized nums, so we also have to normalize target
    # Elems of the subset are not normalized (by specification)
    return memo_table[len(nums)-1][target-min_num]

    # TO BE TESTED


