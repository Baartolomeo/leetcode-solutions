//Time complexity: O(n)
//Space complexity: O(n)

/*Description

Given the root of a Binary Search Tree (BST), return the minimum difference
between the values of any two different nodes in the tree.

Example:
    Input: root = [4,2,6,1,3]
    Output: 1

*/

const int MAX_NODES_DIFF = 1e5 + 1;


class Solution {
public:
    int minDiffInBST(TreeNode* root) {
        std::vector<int> bstNodesVal;
        buildNodeValArrByTraverseTreeInOrder(root, bstNodesVal);
        return getMinInBst(bstNodesVal);
    }


    void buildNodeValArrByTraverseTreeInOrder(TreeNode* node, std::vector<int>& nodesValVector)
    {
        if (!node)
        {
            return;
        }
        buildNodeValArrByTraverseTreeInOrder(node->left, nodesValVector);
        nodesValVector.push_back(node->val);
        buildNodeValArrByTraverseTreeInOrder(node->right, nodesValVector);
    }

    int getMinInBst(std::vector<int>& nodesValVector)
    {
        int minDiffVal = MAX_NODES_DIFF;
        int greaterNodeVal, lowerNodeVal, currNodeVal;
        greaterNodeVal = nodesValVector.back();
        nodesValVector.pop_back();
        while (!nodesValVector.empty())
        {
            lowerNodeVal = nodesValVector.back();
            currNodeVal = greaterNodeVal - lowerNodeVal;
            minDiffVal = currNodeVal < minDiffVal ? currNodeVal : minDiffVal;
            greaterNodeVal = lowerNodeVal;
            nodesValVector.pop_back();
        }
        return minDiffVal;
    }
};