import math

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively,
    return the median of the two sorted arrays.
    The overall run time complexity should be O(log(m+n)).
    """
    m, n = len(nums1), len(nums2)

    # Ensure nums1 is the smaller array for binary search optimization
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m

    # Binary search on the smaller array (nums1)
    low = 0
    high = m
    total_length = m + n

    while low <= high:
        partition1 = (low + high) // 2  # Partition for nums1
        # Calculate partition for nums2 based on partition1
        # (m + n + 1) // 2 ensures that the left parts combined have one more element
        # than the right parts if total_length is odd, making max(maxLeft1, maxLeft2) the median.
        # If total_length is even, left parts have equal elements to right parts.
        partition2 = (total_length + 1) // 2 - partition1

        # Determine the four boundary elements around the partitions
        # (max element on the left and min element on the right for both arrays)

        # If partition1 is 0, it means no elements are in the left part of nums1
        maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
        # If partition1 is m, it means all elements are in the left part of nums1
        minRight1 = nums1[partition1] if partition1 < m else float('inf')

        maxLeft2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
        minRight2 = nums2[partition2] if partition2 < n else float('inf')

        # Check if we have found the correct partition
        # The condition is: max element of left halves <= min element of right halves
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # Correct partition found, now calculate the median
            if total_length % 2 == 1:  # Odd total length
                # The median is the maximum of the elements at the end of the left partitions
                return float(max(maxLeft1, maxLeft2))
            else:  # Even total length
                # The median is the average of the maximum of the left partitions
                # and the minimum of the right partitions
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
        elif maxLeft1 > minRight2:
            # partition1 is too large (elements in nums1's left part are too big)
            # Move left in nums1's search space
            high = partition1 - 1
        else: # maxLeft2 > minRight1
            # partition1 is too small (elements in nums2's left part are too big,
            # meaning we need more from nums1 in its left part)
            # Move right in nums1's search space
            low = partition1 + 1

    # Should not be reached if inputs are valid sorted arrays
    # and the logic is correct, as a median always exists.
    raise ValueError("Input arrays are not sorted or other unexpected error.")


if __name__ == "__main__":
    # Example 1
    nums1_ex1 = [1, 3]
    nums2_ex1 = [2]
    # Combined: [1, 2, 3], Median: 2
    print(f"Nums1: {nums1_ex1}, Nums2: {nums2_ex1}, Median: {findMedianSortedArrays(nums1_ex1, nums2_ex1)}")

    # Example 2
    nums1_ex2 = [1, 2]
    nums2_ex2 = [3, 4]
    # Combined: [1, 2, 3, 4], Median: (2+3)/2 = 2.5
    print(f"Nums1: {nums1_ex2}, Nums2: {nums2_ex2}, Median: {findMedianSortedArrays(nums1_ex2, nums2_ex2)}")

    # Example 3: One array is empty
    nums1_ex3 = []
    nums2_ex3 = [1]
    # Combined: [1], Median: 1
    print(f"Nums1: {nums1_ex3}, Nums2: {nums2_ex3}, Median: {findMedianSortedArrays(nums1_ex3, nums2_ex3)}")

    nums1_ex4 = [2, 3, 4]
    nums2_ex4 = []
    # Combined: [2, 3, 4], Median: 3
    print(f"Nums1: {nums1_ex4}, Nums2: {nums2_ex4}, Median: {findMedianSortedArrays(nums1_ex4, nums2_ex4)}")

    # Example 5: Arrays with different lengths
    nums1_ex5 = [1, 3, 5, 7]
    nums2_ex5 = [2, 4, 6]
    # Combined: [1, 2, 3, 4, 5, 6, 7], Median: 4
    print(f"Nums1: {nums1_ex5}, Nums2: {nums2_ex5}, Median: {findMedianSortedArrays(nums1_ex5, nums2_ex5)}")

    # Example 6: Arrays where one is much larger
    nums1_ex6 = [100]
    nums2_ex6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Combined: [1, 2, ..., 10, 100], Median: (5+6)/2 = 5.5 (if 10 elements, median is avg of 5th and 6th)
    # Total 11 elements. Median is the 6th element, which is 6
    print(f"Nums1: {nums1_ex6}, Nums2: {nums2_ex6}, Median: {findMedianSortedArrays(nums1_ex6, nums2_ex6)}")
    # Corrected combined: [1,2,3,4,5,6,7,8,9,10,100]. Median is 6.

    # Example 7: All elements of one array are smaller than the other
    nums1_ex7 = [1, 2, 3]
    nums2_ex7 = [4, 5, 6]
    # Combined: [1, 2, 3, 4, 5, 6], Median: (3+4)/2 = 3.5
    print(f"Nums1: {nums1_ex7}, Nums2: {nums2_ex7}, Median: {findMedianSortedArrays(nums1_ex7, nums2_ex7)}")

    # Example 8: Identical arrays
    nums1_ex8 = [10, 20]
    nums2_ex8 = [10, 20]
    # Combined: [10, 10, 20, 20], Median: (10+20)/2 = 15
    print(f"Nums1: {nums1_ex8}, Nums2: {nums2_ex8}, Median: {findMedianSortedArrays(nums1_ex8, nums2_ex8)}")

    # Example 9: From LeetCode
    nums1_ex9 = [0,0]
    nums2_ex9 = [0,0]
    # Combined: [0,0,0,0], Median: 0
    print(f"Nums1: {nums1_ex9}, Nums2: {nums2_ex9}, Median: {findMedianSortedArrays(nums1_ex9, nums2_ex9)}")

    # Example 10: Another LeetCode case
    nums1_ex10 = [1]
    nums2_ex10 = [1]
    # Combined: [1,1], Median: 1
    print(f"Nums1: {nums1_ex10}, Nums2: {nums2_ex10}, Median: {findMedianSortedArrays(nums1_ex10, nums2_ex10)}")

    # Example 11
    nums1_ex11 = [1,3]
    nums2_ex11 = [2,7]
    # Combined: [1,2,3,7], Median: (2+3)/2 = 2.5
    print(f"Nums1: {nums1_ex11}, Nums2: {nums2_ex11}, Median: {findMedianSortedArrays(nums1_ex11, nums2_ex11)}")
