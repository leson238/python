def more_than_once(arr):
    result = []
    uniques = set(arr)
    if len(uniques) == len(arr):
        return result
    for unique in uniques:
        if arr.count(unique) > 1:
            result.append(unique)
    return result
print(more_than_once([1,1,1,2,2,3,3,3]))

def printRepeating(arr, n): 
  
    # Store elements and  
    # their counts in 
    # hash table 
    mp = [0] * 100
    for i in range(0, n): 
        print(i)
        mp[arr[i]] += 1
    print(mp)
    # Since we want elements  
    # in same order, we  
    # traverse array again  
    # and print those elements  
    # that appear more than once. 
    for i in range(0, n): 
        if (mp[arr[i]] > 1): 
            print(arr[i], end = " ") 
              
            # This is tricky, this  
            # is done to make sure  
            # that the current element  
            # is not printed again 
            mp[arr[i]] = 0
      
# Driver code 
arr = [12, 10, 9, 45,  
       2, 10, 10, 45]  
n = len(arr) 
printRepeating(arr, n) 