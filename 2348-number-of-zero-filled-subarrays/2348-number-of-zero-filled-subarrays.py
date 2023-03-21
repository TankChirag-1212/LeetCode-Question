class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 and nums[0] != 0:
            return 0
        if n == 1 and nums[0] == 0:
            return 1
        if nums.count(0) == 0:
            return 0
        res = count = 0
        for i in range(n):
            if nums[i] == 0:
                count+=1
            else:
                count = 0
            res += count
            
        return res