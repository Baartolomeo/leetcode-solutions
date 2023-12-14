#Time complexity: O(n)
#Space complexity: O(n)

"""Description:

Given an undirected tree consisting of n vertices numbered from 0 to n-1,
which has some apples in their vertices. You spend 1 second to walk over one
edge of the tree. Return the minimum time in seconds you have to spend to
collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where
edges[i] = [ai, bi] means that exists an edge connecting the vertices ai
and bi. Additionally, there is a boolean array hasApple, where hasApple[i]
= true means that vertex i has an apple; otherwise, it does not have any apple.

Example 1:
    Input:
        n = 7,
        edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
        hasApple = [false,false,true,false,true,true,false]
    Output: 8
    Explanation:
        The figure above represents the given tree where red vertices have an apple.
        One optimal path to collect all apples is shown by the green arrows.

"""

class Solution:

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """Implementation of problem solution.

        :param n: number of tree vertices
        :param edges: array of tree edges
        :param hasApple: boolean array where true means that
                         vertex i has an apple
        :return: minimum time in seconds you have to spend
                 to collect all apples in the tree
        """

        graph = {i: list() for i in range(n)}
        apple_nodes = [i for i in range(n) if hasApple[i]]
        for edge in sorted(edges):
            x, y = edge
            graph[x].append(y)
            graph[y].append(x)

        visited_nodes = set()
        for apple in apple_nodes:
            if apple != 0:
                self.visitNode(visited_nodes, graph, apple, 0)

        return len(visited_nodes) * 2

    def visitNode(self, visit_set, graph, node, prev_node):
        """Recursive function that visit next's nodes in graph.

        Function determines the shortest path in the graph.
        Each node in graph contains table in sorted order so
        from the highest to the lowest vertex in the tree. Function
        adds each visited node to 'visit_set' and route next visited node
        by next element in list. Function ends when reaches the root of
        the tree. To each call of function previously visited node is
        passed in order to avoid cycles.

        :param visit_set: set of visited nodes by the function
        :param graph: dictionary represents graph
        :param node: current visited node
        :param prev_node: previously visited node
        :return: None
        """
        visit_set.add(node)
        for item in graph[node]:
            if prev_node == item:
                continue
            elif item == 0:
                return
            elif item in visit_set:
                return
            self.visitNode(visit_set, graph, item, node)
            return
