class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans, n = [], len(potions)
        for k in spells:
            val = success // k
            if success % k == 0:
                idx = bisect.bisect_left(potions, val)
            else:    
                idx = bisect.bisect_right(potions, val)
            ans.append(n - idx)
        return ans