#Time complexity: O(n)
#Space complexity: O(n)

class Solution:

    def minTime(self, n, edges, hasApple):

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
