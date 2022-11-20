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
    # Lower bound for search: the sum of all negative numbers
    lower_bound = sum([num for num in nums if num < 0])
    # Upper bound for search: the sum of all positive numbers
    upper_bound = sum([num for num in nums if num > 0])

    # Check if target is in bounds
    if (target < lower_bound) or (target > upper_bound):
        return False

    # memo_table[i][j - lower_bound] is the answer to subset_sum(nums[0:i+1], j)
    # 0 <= i < len(nums) and lower_bound <= j <= upper_bound
    number_of_j = upper_bound - lower_bound + 1
    memo_table = [ [False]*(number_of_j)  for _ in range(len(nums)) ]

    # Base case: When i=0, we only look at the first element of nums
    # If nums[0] == j, subset_sum(0, nums[0]) = {nums[0]}
    # If nums[0] != j, subset_sum(0, nums[0]) = False

    # Make sure to normalize the index!
    memo_table[0][nums[0] - lower_bound] = {(nums[0], 0)}

    for i in range(1, len(nums)):
        # Topological order: subproblems for smaller i have been calculated
        for j in range(lower_bound, upper_bound+1):
            # subset_sum(i, j) = subset_sum(i-1, j) if the latter has a soln
            subproblem1 = memo_table[i - 1][j - lower_bound]
            if subproblem1:
                memo_table[i][j - lower_bound] = subproblem1

            # subset_sum(i, j) = nums[i] if nums[i] equals j
            if nums[i] == j:
                memo_table[i][j - lower_bound] = {(nums[i], i)}

            # Consider the subproblem subset_sum(i-1, j-nums[i])
            # Subprob. is only defined if the "if" conditional is satisfied
            # If this subproblem is defined and has a solution, then: 
            # subset_sum(i, j) = solution U {nums[i]}
            if upper_bound > j - nums[i] > lower_bound:
                subproblem2 = memo_table[i - 1][j - nums[i] - lower_bound]
                if subproblem2:
                    new_elem = {(nums[i], i)}
                    memo_table[i][j - lower_bound] = subproblem2.union(new_elem)

            # If none of the above, subset_sum(i, j) = False

    # We also have to normalize the target when searching memo table
    return memo_table[len(nums) - 1][target - lower_bound]


if __name__ == '__main__':
    while True:
        strnums = input("Give an array of integers, size >= 1, delimited with [], each number separated by a comma and a space: ")
        target = input('Give a target integer: ')

        try:
            strnums = strnums.strip('[]').split(', ')
            nums = [int(strnum) for strnum in strnums]
            target = int(target)
        except:
            print('Invalid input\n')
            continue

        print(subset_sum(nums, target))
        prompt = input("Press ! to quit, and any other key to continue: ")
        if prompt == '!':
            break
        else:
            print('\n')
