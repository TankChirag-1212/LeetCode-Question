class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)
        
        while l<r:
            mid = (l + r)//2
            if (arr[mid] -1- mid)< k:
                l = mid+1
            else:
                r = mid
            
        return l+k
    
# we used binary searching method to solve this problem
# we check which side of subarray haves missing value greater than k if missing value is less in left side then increamen the left pointer
# we check the missing values using "arr[mid] - mid" where mid is the index of middle
# we continue untill the left pointer is greater than right pointer
# at last we return the answer as left pointers index + k