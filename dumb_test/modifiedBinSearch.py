def modified_start(lst, n):
    if not lst:
        return -1
    start = 0
    end = len(lst) - 1
    if lst[start] > n or lst[end] < n:
        return -1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] >= n:
            end = mid - 1
        else:
            start = mid + 1
    return start


def modified_end(lst, n):
    if not lst:
        return -1
    start = 0
    end = len(lst) - 1
    if lst[start] > n or lst[end] < n:
        return -1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    return end


lst = 'aaabbbc'
c = 'b'
s = modified_start(lst, c)
e = modified_end(lst, c)
print(e - s + 1)
