class Solution:
    def minimumTime(self, time: List[int], tt: int) -> int:
        
        time.sort()
        l , h = time[0], time[-1]*tt
        # ans = 0
        def canComplete(time, tt, maxT):
            count = 0
            for t in time:
                count += maxT // t
            
            return count >= tt
        
        while l <= h:
            mid = l + (h-l) // 2
        
            if canComplete(time, tt, mid):
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
            
        return ans
    
# first we sorted the time arr as we have to use the binary search to solve this problem.
# the lower bound is the minimun number of time in the time arr and the upper bound is the total time taken by the all bus to complete the trip i.e. max(time)*tt...our answer lies in between the lower__ans___upper.
# the condition to check whether we should search right or left of the array we create a func called canComplete.
# this func checks if the current mid we are on completed how many total trips if it is greater than the tt then we go to the left otherwise at right.
# we calculate the time at that mid using the mid//t suppose its 3 and mid is 2 then the count will be 1 i.e is only 1 trip is done by that bus up until this mid.






