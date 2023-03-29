class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        [-1,-8,0,5,-9]
        
        
        [-9,-8,-1,0,5]
                    1 -> 5
                  1 2 -> 5 + 0 + 5
                1 2 3 -> 5 + 0 + 5 + -1 + 0 + 5
              1 2 3 4
        """
        
        satisfaction.sort()
        N = len(satisfaction)
        
        best = 0
        total = 0 # cumulative sum
        last = 0 # last layer sum
        
        for i in range(N -1, -1, -1):
            last += satisfaction[i]
            total += last
            best = max(best, total)
        return best