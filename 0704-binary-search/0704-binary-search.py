class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if nums.count(target) == 0:
            return -1
        l,r = 0, n-1
        while l <= r:
            mid = (l + r)//2
            # print (l, r, mid)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] > target:
                r = mid - 1
        return -1
                
        