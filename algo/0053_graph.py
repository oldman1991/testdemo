#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/12/20

# graph = {'A': ['B', 'C'],
#          'B': ['C', 'D'],
#          'C': ['D'],
#          'D': ['C', 'G', 'H'],
#          'E': ['F'],
#          'F': ['C']
#          }


class Graph(object):
    def __init__(self):
        self.node_neighbors = {}
        self.visited = {}

    def add_nodes(self, nodelist):
        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        if node not in self.nodes():
            self.node_neighbors[node] = []

    def add_edge(self, edge):
        u, v = edge
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)
            if u != v:
                self.node_neighbors[v].append(u)

    def nodes(self):
        return self.node_neighbors.keys()

    def breadth_first_search(self, root=None):
        """
        BFS查找 广度搜索
        :return:
        """
        queue = []
        order = []

        def bfs():
            while queue:
                node = queue.pop(0)
                self.visited[node] = True
                for n in self.node_neighbors[node]:
                    if (n not in self.visited) and (n not in queue):
                        queue.append(n)
                        order.append(n)

        if root:
            queue.append(root)
            order.append(root)
            bfs()

        for node in self.nodes():
            if node not in self.visited:
                queue.append(node)
                order.append(node)
                bfs()
        self.visited = {}
        print(order)
        return order

    def depth_first_search(self, root=None):
        """
        递归深度搜索
        :param root:
        :return:
        """
        order = []

        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.node_neighbors[node]:
                if n not in self.visited:
                    dfs(n)

        if root:
            dfs(root)

        for node in self.nodes():
            if node not in self.visited:
                dfs(node)
        self.visited = {}
        print(order)
        return order

    def depth_first_search2(self, root=None):
        """
        非递归深度搜索
        :param root:
        :return:
        """
        stack = []
        order = []

        def dfs():
            while stack:
                node = stack.pop()
                for n in self.node_neighbors[node]:
                    if n not in self.visited:
                        order.append(n)
                        stack.append(n)
                        self.visited[n] = True
                        break

        if root:
            stack.append(root)
            order.append(root)
            self.visited[root] = True
            dfs()
        for node in self.nodes():
            if node not in self.visited:
                stack.append(node)
                order.append(node)
                self.visited[node] = True
                dfs()

        self.visited = {}
        print(order)
        return order


if __name__ == "__main__":
    g = Graph()
    g.add_nodes([i + 1 for i in range(8)])
    g.add_edge((1, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 4))
    g.add_edge((2, 5))
    g.add_edge((4, 8))
    g.add_edge((5, 8))
    g.add_edge((3, 6))
    g.add_edge((3, 7))
    g.add_edge((6, 7))
    print("nodes:", g.nodes())
    print("BFS:")
    order = g.breadth_first_search(1)
    print("递归DFS:")
    order = g.depth_first_search(1)
    print("非递归DFS:")
    order = g.depth_first_search2(1)
