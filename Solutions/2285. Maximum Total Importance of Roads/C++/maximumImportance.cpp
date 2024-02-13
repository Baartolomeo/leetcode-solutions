//Time complexity: O(nlogn)
//Space complexity: O(N)

/*Description

You are given an integer n denoting the number of cities in a country.
The cities are numbered from 0 to n - 1.

You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes
that there exists a bidirectional road connecting cities ai and bi.

You need to assign each city with an integer value from 1 to n, where each value can only be used once.
The importance of a road is then defined as the sum of the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the values optimally.

Input:
    n = 5,
    roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output:
    43

Explanation: The figure above shows the country and the assigned values of [2,4,5,3,1].
- The road (0,1) has an importance of 2 + 4 = 6.
- The road (1,2) has an importance of 4 + 5 = 9.
- The road (2,3) has an importance of 5 + 3 = 8.
- The road (0,2) has an importance of 2 + 5 = 7.
- The road (1,3) has an importance of 4 + 3 = 7.
- The road (2,4) has an importance of 5 + 1 = 6.
The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
It can be shown that we cannot obtain a greater total importance than 43.

*/


#include <vector>
#include <map>


#define FROM 0
#define TO 1

struct GraphNode
{
    int neighbours = 0;
    int importance = 0;
};

bool hasMoreNeighbours(GraphNode* first_vertex, GraphNode* second_vertex)
{
    return first_vertex->neighbours < second_vertex->neighbours;
}

class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        std::vector<GraphNode*> vertexes;
        std::map<int, GraphNode*> vertex_map;

        for (int i = 0; i < n; i++)
        {
            GraphNode* vertex = new GraphNode();
            vertexes.push_back(vertex);
            vertex_map[i] = vertex;
        }

        for (auto road: roads)
        {
            vertexes[road[FROM]]->neighbours++;
            vertexes[road[TO]]->neighbours++;
        }

        sort(vertexes.begin(), vertexes.end(), hasMoreNeighbours);

        for (int i = 0, importance = 1; i < vertexes.size(); i++)
            vertexes[i]->importance = importance++;

        long int total_importance = 0;
        for (auto road: roads)
            total_importance += vertex_map[road[FROM]]->importance + vertex_map[road[TO]]->importance;

        return total_importance;
    }
};