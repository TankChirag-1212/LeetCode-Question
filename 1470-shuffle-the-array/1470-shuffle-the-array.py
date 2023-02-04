class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        ans = []
        while i < n:
            ans.append(nums[i])
            ans.append(nums[i+n])
            i+=1
        return ans