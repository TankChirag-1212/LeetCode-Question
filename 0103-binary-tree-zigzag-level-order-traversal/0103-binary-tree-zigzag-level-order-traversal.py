# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        if root is None:
            return root
        arr= []

        while q:
            level = []
            for i in range(len(q)):
                # print(len(q))
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            arr.append(level)
        for i in range(1,len(arr),2):
            arr[i] = reversed(arr[i])
        return arr
    
# we have to use the BFS for this problem to be solved
# first we create the queue and add the root to it and then we run the while loop untill all the node is traveresed and queue is empty
# for loop is used to traverse only in the 1 level at a time after traversing all the nodes in particular level it ends and uses new updated queue length
# at last we use one more for loop to reverse the subarray of all nodes at odd levels and make the change in answer array
