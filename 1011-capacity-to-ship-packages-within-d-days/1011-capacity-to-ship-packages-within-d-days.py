class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,u = max(weights), sum(weights)
        res = u
        
        def canShip(cap):
            ships,currCap = 1, cap
            for w in weights:
                if currCap - w < 0 :
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships<= days
        
        while l <= u:
            cap = (l+u) // 2
            if canShip(cap):
                res = min(res,cap)
                u = cap -1
            else:
                l = cap + 1
        return res
    
# In this problem we have to return the minimum number of capacity given ships can take(all the weights must be considered)
# first we found the lower and upper bound of subarrays of capacity
# then by using brute force approach we check for each capacity whether the condition satisfies or not
# if satisfies update the res variable
# we continue this until the subarray of capacities are not finished
# we use binary searching for traversing the subarray of capacities