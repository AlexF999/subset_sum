"""
Created on 11/20/2022

Author: @AlexF999

Tests for subset_sum.py
"""

import subset_sum
from ...coding.python_testbench.testbench import TestBench

"""
Testing strategy for subset_sum(nums, target): Cover all subdomains of the following partitions, each of which splits the input space into nonoverlapping subdomains that cover the whole input space.

Partition on length of nums:
- Length = 1, target equals the element
= Length = 1, target does not equal the element
- Length > 1

Partition on the elements of nums:
- All elements > 0
- All elements < 0
- All elements = 0
- Otherwise

Partition on target:
- Positive target
- Negative target
- Zero target

Partition on inputs:
- Target > sum(nums: num > 0)
- max(nums) < target <= sum(nums: num > 0)
- min(nums) <= target <= max(nums)
- sum(nums: num < 0) < target < min(nums)
- Target < sum(nums: num < 0)

Partition on output:
- Output is False (no subset exists)
- Output contains one element
- Output contains all elements (and length > 1)
- Output contains between one element and all elements (and length > 1)

Partition on output:
- Output is False
- Output contains the first element of nums
- Output contains the last element of nums (length > 1)
- Output does not contain first or last element of nums (length > 2)
"""


"""
Helper function for testing the subset_sum function. 

'nums' and 'target' are parameters which satisfy the preconditions for subset_sum.
'soln_exists' should be True if there is a solution to subset_sum(nums, target), and False otherwise.

Raises an AssertionError if any of the following are true:
- subset_sum(nums, target) returns False and soln_exists = True
- subset_sum(nums, target) returns a subset and soln_exists = False
- subset_sum(nums, target) returns a subset such that for some (num, index) in the subset, nums[index] != num
- subset_sum(nums, target) returns a subset such that indices are repeated, or some indices are out of range
- subset_sum(nums, target) returns a subset such that the sum of all numbers does not equal target

Otherwise, returns None with no error raised.
"""
def test_ssum(nums: list, target: int, soln_exists: bool):
    actual_output = subset_sum(nums, target)
    actual_soln_exists = bool(actual_output)

    assert bool(actual_output) == soln_exists, "Function does not correctly identify whether solution exists or not: Expected {} but got {}".format(soln_exists, actual_soln_exists)

    # If there is no soln, no need to check whether sum equals target
    if not(soln_exists): return

    indices_seen = set()
    actual_sum = 0
    for (num, index) in actual_output:
        assert not(index in indices_seen), "Function repeats indices: Index {}".format(index)

        assert nums[index] == num, "Function includes indices out of range, or indices which do not match accompanying number: Element {}, {}".format(num, index)

        actual_sum += num
        indices_seen.add(index)

    assert actual_sum == target, "Function does not return subset of numbers which add to target: Expected {}, got {}".format(target, actual_sum)


if __name__ == '__main__':
    pass