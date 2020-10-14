def merge_sorted(A, B, m, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while k >= 0:
        if i < 0:
            for idx_B in range(j+1):
                A[idx_B] = B[idx_B]
        if j < 0:
            break
        if A[i] >= B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1
# O(N)
# Space O(1)
# assume all integer,


A = [1, 3, 5, 7, 7, 7, 0, 0, 0]
B = [2, 4, 6]
merge_sorted(A, B, 6, 3)
print(A)
