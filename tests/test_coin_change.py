import unittest
import sys
import os

# Adjust sys.path to include the parent directory (root of the repo)
# This allows importing from the 'dynamic_programming' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dynamic_programming.coin_change import coin_change

class TestCoinChange(unittest.TestCase):

    def test_basic_case(self):
        """1. Basic case: coins = [1,2,5], amount = 11, expected: 3"""
        self.assertEqual(coin_change([1, 2, 5], 11), 3)

    def test_amount_is_zero(self):
        """2. Amount is 0: coins = [1,2,3], amount = 0, expected: 0"""
        self.assertEqual(coin_change([1, 2, 3], 0), 0)

    def test_amount_cannot_be_made(self):
        """3. Amount cannot be made up: coins = [2], amount = 3, expected: -1"""
        self.assertEqual(coin_change([2], 3), -1)

    def test_single_coin_type_possible(self):
        """4. Single coin type, possible: coins = [3], amount = 9, expected: 3"""
        self.assertEqual(coin_change([3], 9), 3)

    def test_single_coin_type_not_possible(self):
        """5. Single coin type, not possible: coins = [5], amount = 7, expected: -1"""
        self.assertEqual(coin_change([5], 7), -1)

    def test_larger_amount_and_coins(self):
        """6. Larger amounts or more coin types."""
        self.assertEqual(coin_change([1, 5, 10, 25], 137), 8) # 25*5 + 10*1 + 1*2 = 8 coins
        self.assertEqual(coin_change([1, 2, 5], 100), 20) # 5*20 = 20 coins
        self.assertEqual(coin_change([4, 5, 9], 31), 4) # 9*3 + 4*1 = 27+4=31 -> 4 coins. (Or 5*5 + 4*1 +? No. 9,9,9,4)
                                                        # 5*5 = 25, rem 6. Not 4.
                                                        # 9*3 = 27, rem 4. 4*1. So 3+1=4.
                                                        # 9*2 = 18, rem 13. 9*1, rem 4. 4*1. So 2+1+1=4.
                                                        # 9*1 = 9, rem 22. 5*4=20, rem 2. Not 4.
                                                        # 5*6 = 30, rem 1. Not 4.
                                                        # 5*3 = 15, rem 16. 4*4. So 3+4 = 7.
                                                        # 4*x. 4*7 = 28, rem 3. No. 4*6=24, rem 7. No.
                                                        # It should be 4. (e.g. 9+9+9+4)
        self.assertEqual(coin_change([186,419,83,408], 6249), 20) # From LeetCode example

    def test_edge_case_coins_one_amount_zero(self):
        """7. Edge case: coins = [1], amount = 0, expected: 0"""
        self.assertEqual(coin_change([1], 0), 0)

    def test_edge_case_no_coins_amount_one(self):
        """8. Edge case: coins = [], amount = 1, expected: -1"""
        self.assertEqual(coin_change([], 1), -1)

    def test_edge_case_no_coins_amount_zero(self):
        """9. Edge case: coins = [], amount = 0, expected: 0"""
        self.assertEqual(coin_change([], 0), 0)

    def test_amount_smaller_than_any_coin(self):
        """10. Amount is smaller than any coin denomination."""
        self.assertEqual(coin_change([5, 10], 3), -1)

    def test_coins_include_amount(self):
        """11. A coin is equal to the amount."""
        self.assertEqual(coin_change([1, 2, 5, 10], 10), 1)

    def test_no_solution_complex(self):
        """12. More complex case where no solution exists."""
        self.assertEqual(coin_change([7, 8], 5), -1)

    def test_greedy_fails(self):
        """13. Case where a greedy approach would fail, but DP finds optimal."""
        # Greedy with [1,3,4] for amount 6 would be 4+1+1 (3 coins).
        # Optimal is 3+3 (2 coins).
        self.assertEqual(coin_change([1, 3, 4], 6), 2)
        
        # Greedy with [1, 15, 25] for amount 30 would be 25 + 1*5 (6 coins)
        # Optimal is 15+15 (2 coins)
        self.assertEqual(coin_change([1, 15, 25], 30), 2)


if __name__ == '__main__':
    unittest.main()
