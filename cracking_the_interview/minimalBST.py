class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bfs(node):
    from collections import deque
    q = deque()
    q.append(node)
    result = []
    while len(q) > 0:
        curr = q.popleft()
        if curr is not None:
            result.append(curr.data)
            q.append(curr.left)
            q.append(curr.right)
        else:
            result.append(curr)
    return result


def createMinimalBST(arr, start, end):
    if start > end:
        return
    mid = (end + start) // 2
    node = Node(arr[mid])
    node.left = createMinimalBST(arr, start, mid - 1)
    node.right = createMinimalBST(arr, mid + 1, end)
    return node


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bin_tree = createMinimalBST(lst, 0, len(lst) - 1)
print(bfs(bin_tree))
