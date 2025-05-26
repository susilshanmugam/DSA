import unittest
import sys
import os

# Adjust sys.path to include the parent directory (root of the repo)
# This allows importing from the 'array' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from array.median_of_two_sorted_arrays import findMedianSortedArrays

class TestFindMedianSortedArrays(unittest.TestCase):

    def test_example_from_description(self):
        """1. Example from problem description."""
        nums1 = [1, 3]
        nums2 = [2]
        self.assertAlmostEqual(findMedianSortedArrays(nums1, nums2), 2.0)

    def test_even_total_length(self):
        """2. Example with even total length."""
        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertAlmostEqual(findMedianSortedArrays(nums1, nums2), 2.5)

    def test_one_array_empty(self):
        """3. One array is empty."""
        # Case 3a: nums1 is empty
        nums1_a = []
        nums2_a = [1]
        self.assertAlmostEqual(findMedianSortedArrays(nums1_a, nums2_a), 1.0)
        
        nums1_b = []
        nums2_b = [1, 2, 3, 4] # Median is (2+3)/2 = 2.5
        self.assertAlmostEqual(findMedianSortedArrays(nums1_b, nums2_b), 2.5)

        # Case 3b: nums2 is empty
        nums1_c = [2, 3]
        nums2_c = []
        self.assertAlmostEqual(findMedianSortedArrays(nums1_c, nums2_c), 2.5)
        
        nums1_d = [1, 2, 3] # Median is 2
        nums2_d = []
        self.assertAlmostEqual(findMedianSortedArrays(nums1_d, nums2_d), 2.0)

    def test_arrays_with_different_lengths(self):
        """4. Arrays with different lengths."""
        nums1 = [1, 3, 5, 7, 9] # 5 elements
        nums2 = [2, 4, 6]      # 3 elements
        # Combined: [1, 2, 3, 4, 5, 6, 7, 9], Median: (4+5)/2 = 4.5
        self.assertAlmostEqual(findMedianSortedArrays(nums1, nums2), 4.5)

        nums1_b = [100]
        nums2_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Combined: [1,2,3,4,5,6,7,8,9,10,100]. Median is 6 (6th element out of 11)
        self.assertAlmostEqual(findMedianSortedArrays(nums1_b, nums2_b), 6.0)
        # Test with the order swapped as the function handles swapping internally
        self.assertAlmostEqual(findMedianSortedArrays(nums2_b, nums1_b), 6.0)


    def test_all_elements_one_smaller_than_other(self):
        """5. Arrays where all elements of one are smaller than all elements of the other."""
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        # Combined: [1, 2, 3, 4, 5, 6], Median: (3+4)/2 = 3.5
        self.assertAlmostEqual(findMedianSortedArrays(nums1, nums2), 3.5)

        nums1_b = [10, 20, 30]
        nums2_b = [1, 2, 3]
        # Combined: [1, 2, 3, 10, 20, 30], Median: (3+10)/2 = 6.5
        self.assertAlmostEqual(findMedianSortedArrays(nums1_b, nums2_b), 6.5)


    def test_arrays_with_duplicate_numbers(self):
        """6. Arrays with duplicate numbers."""
        nums1 = [0, 0]
        nums2 = [0, 0]
        # Combined: [0, 0, 0, 0], Median: (0+0)/2 = 0.0
        self.assertAlmostEqual(findMedianSortedArrays(nums1, nums2), 0.0)

        nums1_b = [1, 1, 1]
        nums2_b = [1, 1, 1]
        # Combined: [1, 1, 1, 1, 1, 1], Median: (1+1)/2 = 1.0
        self.assertAlmostEqual(findMedianSortedArrays(nums1_b, nums2_b), 1.0)

        nums1_c = [1, 2, 3]
        nums2_c = [2, 3, 4] # Note: 2 and 3 are duplicates
        # Combined: [1, 2, 2, 3, 3, 4], Median: (2+3)/2 = 2.5
        self.assertAlmostEqual(findMedianSortedArrays(nums1_c, nums2_c), 2.5)
        
        nums1_d = [1,1,3,3]
        nums2_d = [1,1,3,3]
        # Combined: [1,1,1,1,3,3,3,3], Median: (1+3)/2 = 2.0
        self.assertAlmostEqual(findMedianSortedArrays(nums1_d, nums2_d), 2.0)

    def test_arrays_with_negative_numbers(self):
        """7. Arrays with negative numbers."""
        nums1 = [-5, -3, -1]
        nums2 = [-4, -2, 0]
        # Combined: [-5, -4, -3, -2, -1, 0], Median: (-3-2)/2 = -2.5
        self.assertAlmostEqual(findMedianSortedArrays(nums1, nums2), -2.5)

        nums1_b = [-10, 5, 10]
        nums2_b = [-5, 0, 15]
        # Combined: [-10, -5, 0, 5, 10, 15], Median: (0+5)/2 = 2.5
        self.assertAlmostEqual(findMedianSortedArrays(nums1_b, nums2_b), 2.5)

    def test_larger_arrays(self):
        """8. Larger arrays."""
        nums1 = list(range(1, 101))  # [1, 2, ..., 100]
        nums2 = list(range(101, 201)) # [101, 102, ..., 200]
        # Combined: [1, ..., 200], Median: (100+101)/2 = 100.5
        self.assertAlmostEqual(findMedianSortedArrays(nums1, nums2), 100.5)

        nums1_b = list(range(0, 1000, 2)) # Even numbers [0, 2, ..., 998] - 500 elements
        nums2_b = list(range(1, 1000, 2)) # Odd numbers [1, 3, ..., 999] - 500 elements
        # Combined sorted: [0, 1, 2, ..., 999] - 1000 elements
        # Median is average of 500th and 501st element (0-indexed: 499 and 500)
        # 500th element is 499, 501st element is 500. Median: (499+500)/2 = 499.5
        self.assertAlmostEqual(findMedianSortedArrays(nums1_b, nums2_b), 499.5)

    def test_challenging_partition_logic(self):
        """9. Cases that might challenge the partitioning logic."""
        nums1 = [1, 2, 3, 4, 5, 6]
        nums2 = [0, 0, 0, 0, 10, 10]
        # Combined: [0,0,0,0,1,2,3,4,5,6,10,10] (12 elements)
        # Sorted: 0,0,0,0,1,2,3,4,5,6,10,10
        # Median: (2+3)/2 = 2.5 (6th and 7th elements are 2 and 3)
        self.assertAlmostEqual(findMedianSortedArrays(nums1, nums2), 2.5)

        nums1_b = [3, 4]
        nums2_b = [1, 2, 5, 6]
        # Combined: [1,2,3,4,5,6], Median: (3+4)/2 = 3.5
        self.assertAlmostEqual(findMedianSortedArrays(nums1_b, nums2_b), 3.5) # Test swapping in function

        nums1_c = [1, 2, 5, 6]
        nums2_c = [3, 4]
        self.assertAlmostEqual(findMedianSortedArrays(nums1_c, nums2_c), 3.5)

        nums1_d = [4,5,6,7,8,9,10]
        nums2_d = [1,2,3]
        # [1,2,3,4,5,6,7,8,9,10] median is (5+6)/2 = 5.5
        self.assertAlmostEqual(findMedianSortedArrays(nums1_d, nums2_d), 5.5)
        
        nums1_e = [1,2,3]
        nums2_e = [4,5,6,7,8,9,10]
        self.assertAlmostEqual(findMedianSortedArrays(nums1_e, nums2_e), 5.5)
        
        nums1_f = [2]
        nums2_f = [1,3,4]
        # [1,2,3,4] median (2+3)/2 = 2.5
        self.assertAlmostEqual(findMedianSortedArrays(nums1_f, nums2_f), 2.5)

if __name__ == '__main__':
    unittest.main()
