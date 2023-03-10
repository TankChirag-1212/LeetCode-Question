# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        #Reservior Sampling
        self.arr = []
        
        current = head
        while current is not None:
            self.arr.append(current.val)
            current = current.next

    def getRandom(self) -> int:
        return self.arr[random.randrange(len(self.arr))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()