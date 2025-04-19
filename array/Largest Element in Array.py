# Given an array arr[]. The task is to find the largest element and return it.
#
# Examples:
#
# Input: arr[] = [1, 8, 7, 56, 90]
# Output: 90
# Explanation: The largest element of the given array is 90.
# Input: arr[] = [5, 5, 5, 5]
# Output: 5
# Explanation: The largest element of the given array is 5.
# Input: arr[] = [10]
# Output: 10
# Explanation: There is only one element which is the largest.
# Constraints:
# 1 <= arr.size()<= 106
# 0 <= arr[i] <= 106

def largest_element(arr):
    max=arr[0]
    for i in arr:
        if i > max:
            max=i
    return max

arr=[123,231232,23123]
print(largest_element(arr))
