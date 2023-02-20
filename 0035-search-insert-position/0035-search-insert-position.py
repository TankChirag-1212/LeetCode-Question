class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        j = n-1
        while i<=j:
            mid = i+(j-i)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid+1
                
        return i
            
# used binary searching to solve this problem in O(logn)
# used 2 pointers i at start and j at the end of nums and mid pointer to check if target lies at left or right side of it
# while stops when j becomes low or equal to i
# mid pointer changes if i or j changes (main trick in this problem was to find the mid pointer's equation)