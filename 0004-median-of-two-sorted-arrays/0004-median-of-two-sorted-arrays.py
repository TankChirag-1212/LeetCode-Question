class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        print(nums)
        n = len(nums)
        if n%2:
            median = nums[(n)//2]
            return median
        else:
            median = (nums[(n-1)//2] + nums[(n)//2])/2
            return median
        
