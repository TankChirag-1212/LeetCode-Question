class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap, heapmax = [], 0
        for n in nums:
            tmp = n
            while n % 2 == 0:
                n //= 2
            heap.append((n, max(tmp, n*2)))
            heapmax = max(heapmax, n)
        
        res = float("inf")
        heapq.heapify(heap)
        while len(heap) == len(nums):
            n, nmax = heapq.heappop(heap)
            res = min(res, heapmax - n)
        
            if n < nmax:
                heapq.heappush(heap, (n*2, nmax))
                heapmax = max(heapmax, n*2)
        return res
    
# The key observation in this problem was that we have to reduce the numbers to its minimun value it can get but from the question we can see that only even numbers can be reduced by dividing with 2
# 2nd observation was that even numbers only decrease and odd numbers only increase
# So we reduce all the even numbers to it lowest until it gets to 1 and multilply it by 2 for once then we append all the values in the heap
# we use minimum heap to store the values and pop the minimum value at every iteration until it reaches the last top most value of it
# we use res variable to store the deviation at every changes in the heap
