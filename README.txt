Contains implementations of the subset-sum problem.

The subset-sum problem:
    Given an array of integers, nums, and an integer, target: Return a subset 
of numbers from the array (no repetitions) which add up to target. The array 
elements may be positive, negative, or zero, as well as the target.

    The exhaustive-search solution to this problem is exponential in the length 
of the array, so each implementation uses a dynamic programming approach,
building up the solution from smaller subproblems.

    Let subset-sum(i, j) be the solution to subset-sum(nums(1, i), j), using 
1-indexing, left and right endpoints inclusive. I.e., is there a subset of the 
first i numbers that sums up to j? Note that if lower_bound is the smallest 
possible sum, and upper_bound is the largest possible sum, then lower_bound <= 
j <= upper_bound.

Then the solution to subset-sum(i, j) equals one of the following:
1. subset-sum(i-1, j) (if this subproblem has a solution)
2. The set {nums(i)} (if nums(i) = j)
3. subset-sum(i-1, j-nums(i)) U {nums(i)} (if this subproblem has a solution)
4. False if none of the above three are satisfied.

    Notice these relations only depend on smaller indices i. We can use a table 
to record the answers to subproblems. 

    Constructing the table will take time O(nX), where n is the length of nums, 
and X = upper_bound - lower_bound. Note that this algorithm is exponential in 
the length of the upper and lower bounds, in bits. As a consequence, if the 
array of integers contains very large or small numbers (e.g., 2^32 or -2^32),
the algorithm will be extremely slow (and may throw an error). However, the 
algorithm is very efficient for reasonably-sized integers, even for large n.
