class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while left <= right:
            m = left + ((right - left) //2)
            if ((m-1 < 0 or nums[m-1] != nums[m]) and (m+1 == len(nums) or nums[m+1] != nums[m])):
                return nums[m]
            leftSubarrSize = m-1 if nums[m-1] == nums[m] else m
            
            if leftSubarrSize%2:
                right = m - 1
            else:
                left = m + 1
                
# Unique way to use binary searching
# In this problem we use two pointer left and right and we calculate mid if left or right of mid is same then we check which side of subarray is of odd length
#  we pick the odd one because it ensures that there will be the answer and repeat the process again
#  While loop stops when left and right pointer becames equal (it is the worst case scenario in binary searching)