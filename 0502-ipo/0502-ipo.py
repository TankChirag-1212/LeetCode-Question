class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()
        q = []
        ptr = 0
        for i in range(k):
            while ptr < n and projects[ptr][0] <= w:
                heappush(q, -projects[ptr][1])
                ptr += 1
            if not q:
                break
            w += -heappop(q)
        return w
    
#  This problem is example of greedy problem, it can be solved optimally by using priority queue only
# in this we use heapq module of python to import as priority queue
# In this problem we have to give the final maximum capital we can get using those projects who has higher profits and fits in the capital 
#  we first created a empty queue and push the fist capital form the list of tuples we created, we incriment the "w" at the end if we choose the project
