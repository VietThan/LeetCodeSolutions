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
class Solution {
public:
    // Reduce memory usage
    // Might be bad for multi-threading?
    int max = -10000;
    int count = 0;
    
    int maxNodes(TreeNode* root , int mx){
        if (root){
            if (root->val >= mx){
                return 1 + maxNodes(root->left, root->val)+maxNodes(root->right, root->val);
            } else {
                return maxNodes(root->left, mx)+maxNodes(root->right, mx);
            }
        }
        return 0;
        
    }
    
    int goodNodes(TreeNode* root) {
        if (root){
            count += maxNodes(root, INT_MIN);
        }
        return count;
    }
    
    
};
