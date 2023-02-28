# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(list)
        
        def dfs(node):
            if not node:
                return "null"
            s = ",".join([str(node.val), dfs(node.right), dfs(node.left)])
            if len(subtrees[s]) == 1:
                res.append(node)
            subtrees[s].append(node)
            return s
        res = []
        dfs(root)
        return res
    
# this problem is only possible to solve using dfs and we can do in both either preorder or postorder way
# we use preorder in this solution because its little bit simple and easy to understand
# first we create the empty default dictionary using collections module and we named it as subtrees which stores the all possible subtrees from the given tree
# then we use dfs function in which we use recursion to store all the subtrees serialization in the hashmap or dict
# we check every time that if the serialization of any subtree is repeated for once then we append the root or the current node we are on and we do this for all the subtrees
# in explanation they use trick to confuse a bit we just have to return the root not the list of the subtree nodes


