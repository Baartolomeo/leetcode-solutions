#Time complexity: O(n)
#Space complexity: O(n)

"""Description

Given the root of a Binary Search Tree (BST), return the minimum difference
between the values of any two different nodes in the tree.

Example:
    Input: root = [4,2,6,1,3]
    Output: 1

"""


class Solution:

    def minDiffInBST(self, root):
        """Implementation of problem solution.

            :param root: reference to root node of BST tree.
            :return: minimum difference between the values of
                    any two different nodes in the tree.
        """
        MAX_VALUE = 1e5 + 1
        nodes_value_list = []
        build_list_by_traverse_tree_inOrder(root, nodes_value_list)
        min_diff = MAX_VALUE
        for i in range(len(nodes_value_list) - 1, 0, -1):
            if (diff := nodes_value_list[i] - nodes_value_list[i - 1]) < min_diff:
                min_diff = diff
        return min_diff


def build_list_by_traverse_tree_inOrder(node, nodes_value_list):
    """Recurrence function for building list of nodes value in order.

        :param node: reference to node of BST tree.
        :param nodes_value_list: reference to list of nodes values.
    """
    if not node:
        return
    build_list_by_traverse_tree_inOrder(node.left, nodes_value_list)
    nodes_value_list.append(node.val)
    build_list_by_traverse_tree_inOrder(node.right, nodes_value_list)
