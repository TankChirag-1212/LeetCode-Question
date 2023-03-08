class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        
        if len(piles) == h:
            return high
        
        def canFinish(piles, speed, h):
            count = 0
            for maxB in piles:
                if maxB%speed == 0:
                    count += maxB//speed
                else:
                    count += (maxB//speed) +1
            if count > h:
                return False
            return True
        
        while low <= high:
            mid = low+(high-low)//2

            if canFinish(piles, mid, h):
                k = mid
                high = mid-1
            else:
                low = mid+1
        return k
    
'''
In this problem we have to return the number of bananas koko can eat within one hours i.e. speed of koko eating bananas such that all the bananas are eaten by koko before the given h hours
here the lower bound is 1 banana per hour because if the given h is the sum(piles) then koko can eat 1 banana per hour and still will be able to finish all piles.
and higher bound is the max(piles) because if the h and len(piles) are same then she must finish the max banana's as possible per hour before guards return
We can use brute force approach but it takes more time complexity...so we use binary search to solve this problem
the condition to check whether to jump left or right is to check that at mid/speed is there any banana remains at last or is the speed is too fast.
'''



