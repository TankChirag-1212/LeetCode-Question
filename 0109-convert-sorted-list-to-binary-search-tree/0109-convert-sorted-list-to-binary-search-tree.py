# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def getMiddle(head):
            preHead = ListNode(-1000000000, head)
            fast = preHead
            slow = preHead
            pre = slow
            
            while fast.next is not None:
                fast = fast.next
                if fast.next is not None:
                    fast = fast.next
                pre = slow
                slow = slow.next
            return pre
        
        def toBST(node):
            if node is None:
                return None
            middle_pointer = getMiddle(node)
            
            middle = middle_pointer.next
            middle_pointer.next = None
            if middle is None:
                return TreeNode(node.val)
                
            current = TreeNode(middle.val)
            
            if node != middle:
                current.left = toBST(node)
            current.right = toBST(middle.next)
            
            return current
        
        return toBST(head)