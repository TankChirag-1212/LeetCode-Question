# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
# BFS APPROACH =>

        if not root:
            return 0
        Num_Nodes = deque([root])
        node_At_Level = 1
        levels = 0
        while Num_Nodes:
            node = Num_Nodes.popleft()
            if node.left:
                Num_Nodes.append(node.left)
            if node.right:
                Num_Nodes.append(node.right)
            node_At_Level -= 1
            if node_At_Level == 0:
                levels += 1
                node_At_Level = len(Num_Nodes)
                
        return levels


# DFS APPROAcH =>

#       def dfs(root):
#           if root == None:
#               return 0
#           l = 1 + dfs(root.left)
#           r = 1 + dfs(root.right)
#           return max(l,r)
#       return dfs(root)