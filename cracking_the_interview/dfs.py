from collections import defaultdict


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.depth = 0


def dfs(node):
    if node is None:
        print("None")
        return
    print(node.data)
    dfs(node.left)
    dfs(node.right)


def bfs(node):
    if node is None:
        print("None")
        return
    from collections import deque, defaultdict
    q = deque()
    q.append(node)
    res = defaultdict(list)
    d = 0
    while len(q) > 0:
        n = q.popleft()
        d = max(d, n.depth)
        res[n.depth].append(n)
        left = n.left

        if left is not None:
            left.depth = n.depth + 1
            q.append(left)
        else:
            res[n.depth + 1].append(None)
        right = n.right

        if right is not None:
            right.depth = n.depth + 1
            q.append(right)
        else:
            res[n.depth + 1].append(None)
    d += 1
    for record in sorted(res.items()):
        if record[0] == d:
            break
        print(f"level {record[0]}: ", end='')
        buffer = ' ' * ((2**(d - record[0])) // 2)
        for v in record[1]:
            if v is not None:
                print(f"{buffer}{v.data}{buffer}", end='')
            else:
                print(f"{buffer}N{buffer}", end='')
        print('\n')


def max_depth(node):
    if node is None:
        return 0
    m_depth = max(max_depth(node.left), max_depth(node.right))
    return m_depth + 1


def generate_tree():
    from random import randint
    from collections import deque
    f = randint
    root = Node(f(1, 10))
    q = deque()
    q.append(root)
    i = 0
    while len(q) > 0 and i <= 32:
        n = q.popleft()
        l_value = f(0, 10)
        if l_value == 0:
            n.left = None
        else:
            n.left = Node(l_value)
            q.append(n.left)
            i += 1
        r_value = f(0, 10)
        if r_value == 0:
            n.right = None
        else:
            n.right = Node(r_value)
            q.append(n.right)
            i += 1
    # root.left.left = Node(f(1, 10))
    # root.left.right = Node(f(1, 10))
    # root.right.right = Node(f(1, 10))
    # root.left.right.left = Node(f(1, 10))
    return root


def driver_dfs():
    root = generate_tree()
    dfs(root)


def driver_max_depth():
    root = generate_tree()
    bfs(root)
    print(f'depth: {max_depth(root)}')


driver_max_depth()


class Graph:

    def __init__(self):
        self.vertices = defaultdict(lambda: set())

    def addEdge(self, u, v):
        self.vertices[u].add(v)


def route_between_nodes(graph, node, node_to_find):
    visited = set()
    result = []

    def dfs_graph(graph, node, node_to_find):
        visited.add(node)
        if node is None:
            return
        if node is node_to_find:
            result.append(True)
        for n in graph.vertices[node]:
            if n not in visited:
                dfs_graph(graph, n, node_to_find)
    dfs_graph(graph, node, node_to_find)
    visited.clear()
    dfs_graph(graph, node_to_find, node)
    if True in result:
        return True
    return False


def driver_find_route():
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 4)
    g.addEdge(2, 3)
    g.addEdge(2, 5)
    print(route_between_nodes(g, 1, 5))
    print(route_between_nodes(g, 1, 3))
    print(route_between_nodes(g, 4, 5))
