class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        q = deque()
        visited = [False]*n
        
        heap = collections.defaultdict(list)
        
        for i, x in enumerate(arr):
            heap[x].append(i)
        
        q.append(0)
        visited[0] = True
        ans = 0
        while q:
            for size in range(len(q), 0, -1):
                i = q.popleft()
                if i == n-1:
                    return ans
                nextValue = heap[arr[i]]
                nextValue.append(i+1)
                nextValue.append(i-1)
                for j in nextValue:
                    if 0 < j < n and not visited[j]:
                        visited[j] = True
                        q.append(j)
                heap[arr[i]].clear()
            ans+=1
        return 0
        
# first we create the hash map to store the indices of the occurence of elemnt in the arr
# then we create queue and visited arr to keep track of the visited node
# then we add the 0th index in the queue and visited
# we run the while loop until we traverse all the elements in the arr(this is worst case scenario)
# we pop the left element and we store in i.. then we check if the i is last index in the arr if it is return ans or else continue
# we create the nextValue arr to store the left, right and jth index(index of 2nd apperance in the arr) of that element.
# then we run the for loop and check if the next value is valid to visit or not if it is then we append that into the queue and visited
# then we clear the list of indices of that element in the heap to reduce the repeatation
# we increament ans after we traverse each level in bfs tree....and finally return the ans if we reach the end of arr or we will return 0
















