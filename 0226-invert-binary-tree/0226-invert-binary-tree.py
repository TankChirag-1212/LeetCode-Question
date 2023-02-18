# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node is None:
                break
            temp = node.right
            node.right = node.left
            node.left = temp
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return root
    
# first we created queue to store the root node in it then we pop root and saved into node
# then we use the temp node and swap the right and left child of the current node
# after doing that we update the new right and left child in the root and append them in the queue
# while loop stops when all the nodes are traversed which means the queue is none/empty
# this approach is bfs approach in reverse traversing
