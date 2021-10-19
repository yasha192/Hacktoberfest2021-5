#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

def maxWater(arr, n):
    # indices to traverse the array
    left = 0
    right = n-1
 
    # To store Left max and right max
    # for two pointers left and right
    l_max = 0
    r_max = 0
 
    # To store the total amount
    # of rain water trapped
    result = 0
    while (left <= right):
         
        # We need check for minimum of left
        # and right max for each element
        if r_max <= l_max:
             
            # Add the difference between
            #current value and right max at index r
            result += max(0, r_max-arr[right])
             
            # Update right max
            r_max = max(r_max, arr[right])
             
            # Update right pointer
            right -= 1
        else:
             
            # Add the difference between
            # current value and left max at index l
            result += max(0, l_max-arr[left])
             
            # Update left max
            l_max = max(l_max, arr[left])
             
            # Update left pointer
            left += 1
    return result
 
 
# Driver code
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
print(maxWater(arr, n))