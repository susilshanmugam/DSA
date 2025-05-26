import unittest
import sys
import os

# Adjust sys.path to include the parent directory (root of the repo)
# This allows importing from the 'linked_list_problems' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# The ListNode class and helper functions are defined in merge_k_sorted_lists.py
from linked_list_problems.merge_k_sorted_lists import Solution, ListNode, list_to_linked_list, linked_list_to_list
from typing import List, Optional

class TestMergeKSortedLists(unittest.TestCase):

    def setUp(self):
        """Create a new Solution instance for each test."""
        self.solver = Solution()

    def run_test(self, lists_of_lists: List[List[int]], expected_list: List[int]):
        """
        Helper function to run a test case.
        Converts lists of integers to lists of ListNodes, calls mergeKLists,
        and then converts the result back to a list of integers for comparison.
        """
        input_linked_lists: List[Optional[ListNode]] = []
        for l_val in lists_of_lists:
            input_linked_lists.append(list_to_linked_list(l_val))
        
        merged_head = self.solver.mergeKLists(input_linked_lists)
        result_list = linked_list_to_list(merged_head)
        
        self.assertEqual(result_list, expected_list, 
                         f"Input: {lists_of_lists}, Expected: {expected_list}, Got: {result_list}")

    def test_basic_example(self):
        """1. Basic example: lists = [[1,4,5],[1,3,4],[2,6]]"""
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        expected = [1, 1, 2, 3, 4, 4, 5, 6]
        self.run_test(lists, expected)

    def test_empty_list_of_lists(self):
        """2. Empty list of lists: lists = []"""
        lists = []
        expected = []
        self.run_test(lists, expected)

    def test_list_with_some_empty_lists(self):
        """3. List of lists containing some empty lists: lists = [[], [1]]"""
        lists1 = [[], [1]]
        expected1 = [1]
        self.run_test(lists1, expected1)

        lists2 = [[1, 3], [], [2, 4]]
        expected2 = [1, 2, 3, 4]
        self.run_test(lists2, expected2)
        
        lists3 = [[], [], [1,2,3], [], []]
        expected3 = [1,2,3]
        self.run_test(lists3, expected3)

    def test_list_with_all_empty_lists(self):
        """4. List of lists where all are empty: lists = [[], [], []]"""
        lists = [[], [], []]
        expected = []
        self.run_test(lists, expected)

    def test_lists_with_single_elements(self):
        """5. Lists with single elements."""
        lists1 = [[10], [1], [100]]
        expected1 = [1, 10, 100]
        self.run_test(lists1, expected1)

        lists2 = [[5]]
        expected2 = [5]
        self.run_test(lists2, expected2)
        
        lists3 = [[-1], [-5], [0]]
        expected3 = [-5, -1, 0]
        self.run_test(lists3, expected3)

    def test_lists_with_varying_lengths(self):
        """6. Lists with varying lengths."""
        lists1 = [[1, 2, 3, 10, 20], [4, 5], [6, 7, 8]]
        expected1 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 20]
        self.run_test(lists1, expected1)

        lists2 = [[1], [1, 2, 3, 4, 5], [10, 20]]
        expected2 = [1, 1, 2, 3, 4, 5, 10, 20]
        self.run_test(lists2, expected2)

    def test_one_list_is_significantly_longer(self):
        """Test with one list much longer than others."""
        lists = [[1, 1, 1, 1, 100], [2, 3, 4]]
        expected = [1, 1, 1, 1, 2, 3, 4, 100]
        self.run_test(lists, expected)

    def test_lists_with_negative_numbers(self):
        """Test with lists containing negative numbers."""
        lists = [[-2, -1, 0], [-5, -3], [1, 2, 3]]
        expected = [-5, -3, -2, -1, 0, 1, 2, 3]
        self.run_test(lists, expected)

    def test_lists_already_sorted_among_themselves(self):
        """Test where the first elements of lists are already in order."""
        lists = [[1, 5], [10, 15], [20, 25]]
        expected = [1, 5, 10, 15, 20, 25]
        self.run_test(lists, expected)

    def test_lists_in_reverse_order_of_first_elements(self):
        lists = [[20, 25], [10, 15], [1, 5]]
        expected = [1, 5, 10, 15, 20, 25]
        self.run_test(lists, expected)

if __name__ == '__main__':
    unittest.main()
