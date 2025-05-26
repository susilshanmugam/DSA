def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    Approach:
    1. Create a dictionary to store the numbers encountered so far and their indices.
    2. Iterate through the input array `nums` with both index and value.
    3. For each number, calculate its complement (target - current_number).
    4. Check if the complement exists as a key in the dictionary.
       - If it does, it means we have found the two numbers that add up to the target.
         Return the index of the complement (stored in the dictionary) and the current number's index.
       - If it doesn't, add the current number and its index to the dictionary.
    5. This approach ensures that we find the solution in a single pass, with an average time complexity of O(n)
       because dictionary lookups and insertions take O(1) on average.
    We assume that each input would have exactly one solution and we may not use the same element twice.
    """
    num_to_index = {}  # Dictionary to store number and its index
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            # Found the complement in our dictionary
            return [num_to_index[complement], index]
        # Add the current number and its index to the dictionary
        num_to_index[num] = index
    return [] # Should not be reached given the problem constraints (exactly one solution)

if __name__ == "__main__":
    # Example 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Nums: {nums1}, Target: {target1}, Indices: {result1}") # Expected: [0, 1] or [1, 0]

    # Example 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"Nums: {nums2}, Target: {target2}, Indices: {result2}") # Expected: [1, 2] or [2, 1]

    # Example 3
    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum(nums3, target3)
    print(f"Nums: {nums3}, Target: {target3}, Indices: {result3}") # Expected: [0, 1] or [1, 0]

    # Example 4 with negative numbers
    nums4 = [-1, -3, 5, 7, 10]
    target4 = 2
    result4 = two_sum(nums4, target4)
    print(f"Nums: {nums4}, Target: {target4}, Indices: {result4}") # Expected: [1, 2] (for -3 + 5 = 2)

    # Example 5: target is zero
    nums5 = [-2, 7, 2, 15]
    target5 = 0
    result5 = two_sum(nums5, target5)
    print(f"Nums: {nums5}, Target: {target5}, Indices: {result5}") # Expected: [0, 2] (for -2 + 2 = 0)
