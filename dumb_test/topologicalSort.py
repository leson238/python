from collections import defaultdict
lst = [('a', 'b'), ('c', 'd'), ('c', 'a'), ('d', 'e'),
       ('g', 'd'), ('e', 'f'), ('k', 'h')]


class Graph:
    def __init__(self, edge_lst=None):
        self.vertices, self.adj_lst = set(), defaultdict(set)

    def addEdge(self, lst):
        adj_lst = defaultdict(set)
        vertices = set()
        if lst:
            for pair in lst:
                start, to = pair
                adj_lst[to].add(start)
                vertices.add(start)
                vertices.add(to)
                self.vertices.add(start)
                self.vertices.add(to)
                self.adj_lst[to].add(start)
        return vertices, adj_lst

    def topological_sort(self):
        return []

    def __str__(self):
        res = ""
        for vertex in self.adj_lst:
            res += f"{vertex} <- {[x for x in self.adj_lst[vertex]]}\n"
        return res


g = Graph()
vertices, adj_lst = g.addEdge(lst)
# adj_lst = g.adj_lst.copy()


def topological_sort(vertices, adj_lst):
    res = []
    cycle = False
    # while there are still tasks not done
    while vertices:
        # break if found a cycle
        if cycle:
            break
        # tasks without prerequisites
        temp_res = []
        for vertex in vertices:
            if not adj_lst[vertex]:
                temp_res.append(vertex)
        # remove tasks without prequisites from tasks list and tasks dict, emulate the fact that they are done
        for vertex in temp_res:
            vertices.discard(vertex)
            del adj_lst[vertex]
        for vertex in adj_lst:
            for from_vertex in temp_res:
                adj_lst[vertex].discard(from_vertex)
        # if there is no tasks can be removed while still have tasks not completed, that's mean there's a cycle
        if not temp_res:
            print("Cycle detected")
            cycle = True
        res += temp_res
    if cycle:
        res = -1
    return res


print(topological_sort(vertices, adj_lst))
print(g)
print(g.vertices)
