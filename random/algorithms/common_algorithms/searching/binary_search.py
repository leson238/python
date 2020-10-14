def binary_search(arr, l, r, x):
    m = l + (r-l)//2
    if r >= l:
        if x == arr[m]:
            return m 
        elif x > arr[m]:
            return binary_search(arr, m+1, r, x)
        else:
            return binary_search(arr, l, m-1, x)
    else:
        return -1

arr = [1,2,3,4,5,6]
print(binary_search(arr,0, len(arr)-1, 5))

# Work on sorted data
# No inplace modification of array
# O(logN)