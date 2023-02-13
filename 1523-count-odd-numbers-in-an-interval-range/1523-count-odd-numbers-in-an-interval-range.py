class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        if low%2 == 0:
            count = high - low+1
            count = (count)//2
            return count
        
        count = high - low +1
        count = (count + 1)//2
        
        return count