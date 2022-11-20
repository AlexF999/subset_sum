"""
Created on 11/20/2022

Author: @AlexF999

Tests for subset_sum.py
"""

import subset_sum

"""
A class for packaging multiple tests into one testbench.
"""
class TestBench:
    """
    Class constructor.

    description: A string description of the testbench as a whole.
    """
    def __init__(self, description: str):
        self.description = description

        # Rep. Invariant: The elems of __test are dictionary with the following key/value pairs:
        # "description": string description of test
        # "function": Pointer to the function for this test
        # "Inputs": The parameters to pass to this function
        self.__tests = []

    """
    funct: A pointer to a function to run as part of the testbench. It may have any output, but the output will be ignored when running the testbench.
    inputs: The parameters to be passed to the function. The length of inputs should match the number of parameters of the function.
    descripion: A string description of this particular test
    """
    def add_test(self, funct: function, inputs: list, description: str):
        test = {'description': description, 'function': funct, 'inputs': inputs}
        self.__tests.append(test)

    """
    Runs all of the tests in the testbench
    """
    def run_bench(self):
        print("{}\n".format(self.description))
        for test_id in range(len(self.__tests)):
            test = self.__tests[test_id]
            description, test_function, test_parameters = test['description'], test['function'], test['inputs']
            print("Running test {}\n".format(test_id))
            print("Description: {}\n".format(description))
            assert test_function(*test_parameters)
            print("Test {} okay\n\n".format(test_id))



"""
Testing strategy for subset_sum(nums, target): Cover all subdomains of the following partitions, each of which splits the input space into nonoverlapping subdomains that cover the whole input space.

Partition on length of nums:
- Length = 1
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

Partition on output:
- Output is False (no subset exists)
- Output contains one element
- Output contains all elements (length > 1)
- Output contains between one and all elements (length > 1)

Partition on output:
- Output is False
- Output contains the first element of nums
- Output contains the last element of nums (length > 1)
- Output does not contain first or last element of nums (length > 2)
"""
