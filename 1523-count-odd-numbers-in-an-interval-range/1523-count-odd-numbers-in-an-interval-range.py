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
    
    
    # ANOTHER SOLUTION (ONE LINER)
    class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low)//2 + (high%2 or low % 2)    # (high % 2 or low % 2) this gives the value 1 if either one of low or high is odd, it gives 0 if both the low and high is even
        return count
