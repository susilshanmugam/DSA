import unittest
import sys
import os

# Adjust sys.path to include the parent directory (root of the repo)
# This allows importing from the 'array' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from array.two_sum import two_sum

class TestTwoSum(unittest.TestCase):

    def assertIndicesEqual(self, result, expected1, expected2):
        """Helper assertion to check if result matches one of two expected index pairs."""
        self.assertTrue(result == expected1 or result == expected2,
                        f"Expected {expected1} or {expected2}, but got {result}")

    def test_basic_case(self):
        """Test a basic case with a solution."""
        nums = [2, 7, 11, 15]
        target = 9
        expected_indices1 = [0, 1]
        expected_indices2 = [1, 0]
        result = two_sum(nums, target)
        self.assertIndicesEqual(sorted(result), sorted(expected_indices1), sorted(expected_indices2))

    def test_negative_numbers(self):
        """Test a case with negative numbers."""
        nums = [-1, -3, 7, 2]
        target = -4
        expected_indices1 = [0, 1]
        expected_indices2 = [1, 0]
        result = two_sum(nums, target)
        self.assertIndicesEqual(sorted(result), sorted(expected_indices1), sorted(expected_indices2))

    def test_repeated_numbers_distinct_elements_solution(self):
        """Test a case with repeated numbers, but the solution uses distinct elements."""
        nums = [3, 3, 4]
        target = 6 # Should pick the two 3s
        expected_indices1 = [0, 1]
        expected_indices2 = [1, 0]
        result = two_sum(nums, target)
        self.assertIndicesEqual(sorted(result), sorted(expected_indices1), sorted(expected_indices2))

    def test_target_is_zero(self):
        """Test a case where the target is zero."""
        nums = [-2, 7, 2, 15]
        target = 0
        expected_indices1 = [0, 2]
        expected_indices2 = [2, 0]
        result = two_sum(nums, target)
        self.assertIndicesEqual(sorted(result), sorted(expected_indices1), sorted(expected_indices2))

    def test_no_solution(self):
        """Test a case where no two numbers sum up to the target.
        The problem statement implies there's always one solution,
        but good to test this edge case for robustness if constraints change.
        The current two_sum returns [] if no solution is found.
        """
        nums = [1, 2, 3, 4]
        target = 10
        result = two_sum(nums, target)
        self.assertEqual(result, [])

    def test_example_from_implementation_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = two_sum(nums, target)
        self.assertTrue(sorted(result) == [0,1])

    def test_example_from_implementation_2(self):
        nums = [3,2,4]
        target = 6
        result = two_sum(nums, target)
        self.assertTrue(sorted(result) == [1,2])

    def test_example_from_implementation_3(self): # Same as repeated_numbers
        nums = [3,3]
        target = 6
        result = two_sum(nums, target)
        self.assertTrue(sorted(result) == [0,1])


if __name__ == '__main__':
    unittest.main()
