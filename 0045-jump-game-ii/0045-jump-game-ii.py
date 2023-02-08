class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        Jump = 0
        curr = 0

        for i in range(len(nums)-1):
            furthest = max(furthest, i + nums[i])
            if curr == i:
                curr = furthest
                Jump += 1
        return Jump