/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

#include <queue>

class Solution {
public:
    bool btreeGameWinningMove(TreeNode* root, int n, int x) {
        bool result = false;
        TreeNode* xNode = SearchForNodeWithVal(root, x);
        int left_subtree_no_nodes_attached = 0;
        int right_subtree_no_nodes_attached = 0;

        if (xNode->left)
        {
            left_subtree_no_nodes_attached = get_no_nodes_attached(xNode->left);
            left_subtree_no_nodes_attached++;
        }

        if (xNode->right)
        {
            right_subtree_no_nodes_attached = get_no_nodes_attached(xNode->right);
            right_subtree_no_nodes_attached++;
        }

        if ((n - (left_subtree_no_nodes_attached + right_subtree_no_nodes_attached + 1)) > (n / 2))
        {
            result = true;
        }
        else
        {
            int nodes_from_root_to_x = n - (right_subtree_no_nodes_attached + left_subtree_no_nodes_attached + 1);
            if ((right_subtree_no_nodes_attached > (left_subtree_no_nodes_attached + 1 + nodes_from_root_to_x)) || (left_subtree_no_nodes_attached > (right_subtree_no_nodes_attached + 1 + nodes_from_root_to_x)))
            {
                result = true;
            }
        }

        return result;
    }

private:

    TreeNode* SearchForNodeWithVal(TreeNode* root, int val)
    {
        TreeNode* ValNode = root;
        if (ValNode->val != val)
        {
            std::queue<TreeNode*> q;
            if (ValNode->left)
            {
                q.push(ValNode->left);
            }

            if (ValNode->right)
            {
                q.push(ValNode->right);
            }

            if (!q.empty())
            {
                ValNode = q.front();
                q.pop();

                while (ValNode->val != val)
                {
                    if (ValNode->left)
                    {
                        q.push(ValNode->left);
                    }

                    if (ValNode->right)
                    {
                        q.push(ValNode->right);
                    }
                    ValNode = q.front();
                    q.pop();
                }
            }
        }

        return ValNode;
    }

    int get_no_nodes_attached(TreeNode* start_node)
    {
        int nodes_attached = 0;
        TreeNode* node = start_node;
        std::queue<TreeNode*> q;
        if (node->left)
        {
            q.push(node->left);
            nodes_attached++;
        }

        if (node->right)
        {
            q.push(node->right);
            nodes_attached++;
        }

        if (!q.empty())
        {
            node = q.front();
            while (!q.empty())
            {
                q.pop();
                if (node->left)
                {
                    q.push(node->left);
                    nodes_attached++;
                }

                if (node->right)
                {
                    q.push(node->right);
                    nodes_attached++;
                }
                node = q.front();
            }
        }

        return nodes_attached;
    }

};