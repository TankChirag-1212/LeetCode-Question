# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
    # Time Complexity O(n) -->
        inorderIdx = {v:i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return None
            root = TreeNode(postorder.pop())
            idx = inorderIdx[root.val]

            root.right = helper(idx+1, r)
            root.left = helper(l,idx-1)
            return root

        return helper(0, len(inorder)-1)
        
        
        
# Time Complexity O(n*2) -->
    '''
    if not inorder:
        return None
        
    root = TreeNode(postorder.pop())
    
    idx = inorder.index(root.val)
    
    root.right = self.buildTree(inorder[idx+1:], postorder)
    root.left = self.buildTree(inorder[:idx], postorder)
    return root
    
    '''

'''
• In this problem we have to return the binary tree we created using the inorder and postorder traversal of that tree
• first we confirm the root of our tree....it can be found by checking the last value in the postorder which is always root
• now we first try to solve the right subtree of our binary tree...in postorder just left to the root is always the right child of the root....however we are not sure that its the right child or left child so we use inorder list to check whether the node is at the right of the root or not if it is then its the right child
• similarly we use inorder list to check whether node lies on the right or left of the root and we use postorder list to choose the next node
• the approach of solving this problem is divide and conquer we alway try to solve the right subtree first recursively
'''