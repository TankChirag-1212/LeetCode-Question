# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        
        while q:
            node = q.popleft()
            
            if node:
                q.append(node.left)
                q.append(node.right)
            else:
                while q:
                    if q.popleft():
                        return False
        return True
    
'''
• we have to return boolean value by checking that whether the given tree is complete binary tree or not
• the best approch would be BFS because we have to traverse the tree in level wise from left to right
• we check if the node we poped is null or not if not then we append the childrens into the queue and if its null then else statement executes
• in else statement we run the while until the queue is empty..when the while loop in else statement is running we are checking for the consecutive null values if we found any node then we return the False because its not the complete binary tree
• if we get all the null values at the last then its the complete binary tree and we return the True value
'''