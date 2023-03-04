class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        count = 0
        lastInvalidIdx, lastMinIdx, lastMaxIdx = -1, -1, -1
        
        for i in range(n):
            if nums[i] >= minK and nums[i] <= maxK:
                lastMinIdx = i if nums[i] == minK else lastMinIdx
                lastMaxIdx = i if nums[i] == maxK else lastMaxIdx
                count += max(0, min(lastMinIdx, lastMaxIdx) - lastInvalidIdx)
            else:
                lastInvalidIdx = i
                lastMinIdx = -1
                lastMaxIdx = -1
        return count