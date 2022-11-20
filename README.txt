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
first i numbers that sums up to j?

Then the solution to subset-sum(i, j) equals one of the following:
1. subset-sum(i-1, j) (if this subproblem has a solution)
2. The set {nums(i)} (if nums(i) = j)
3. subset-sum(i-1, j-nums(i)) U {nums(i)} (if this subproblem has a solution)
4. False if none of the above three are satisfied.

    Notice these relations only depend on smaller indices i. We can use a table 
to record the answers to subproblems. 

    Constructing the table will take time O(nT), where n is the length of nums, 
and T is the value of target. Note that this algorithm is still exponential in 
the length of the input, T, in bits. As a consequence, if T were set to a very 
large number, such as 2^32, this algorithm would be extremely slow. However, 
for large n and small T, it runs much more quickly than the exhaustive-search 
approach.
