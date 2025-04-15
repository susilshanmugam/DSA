my_array = [7, 12, 9, -4, 11]
# Given an array of integer, find the min value in it

# Algo:
# Take the first element as minval and iterate through all elements in the list
# If iterate element vale us less than the min make than min else continue till end

min_val = my_array[0]
for i in my_array:
    if i < min_val:
        min_val = i
print("Lowest values is ",min_val)