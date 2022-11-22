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
        self.__description = description
        self.__num_tests = 0

        # Rep. Invariant: The elems of __test are dictionary with the following key/value pairs:
        # "description": string description of test
        # "function": Pointer to the function for this test
        # "Inputs": The parameters to pass to this function
        self.__tests = []

    """
    Add a test to the testbench.

    descripion: A string description of this particular test
    funct: A pointer to a function to run as part of the testbench. It may have any output, but the output will be ignored when running the testbench. The function should *not* have any parameters.
    """
    def add_test(self, description: str, funct):
        test = {'description': description, 'function': funct}
        self.__tests.append(test)
        self.__num_tests += 1

    """
    Add multiple tests to the testbench.

    The tests should be in the form of a list of tuples (description, function), where description and function satisfy the preconditions in add_test.
    """
    def add_tests(self, tests: list):
        for test in tests:
            self.add_test(test[0], test[1])

    """
    Runs all of the tests in the testbench

    Every test will be run, even if some fail.

    The function provided for each test will be run as-is, and the test will pass if the function does not throw an exception.
    """
    def run_bench(self):
        num_passed = 0
        print("{}\n".format(self.__description))

        for test_id in range(len(self.__tests)):
            test = self.__tests[test_id]
            description, test_function = test['description'], test['function']
            print("Running test {}".format(test_id))
            print("Description: {}".format(description))
            try:
                test_function()
                print("Test {} passed\n".format(test_id))
                num_passed += 1
            except Exception as msg:
                print(msg)
                print("Test {} failed\n".format(test_id))
        
        print('{} tests passed, {} tests failed'.format(num_passed, self.__num_tests - num_passed))


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


if __name__ == '__main__':
    pass