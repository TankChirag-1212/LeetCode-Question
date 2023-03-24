class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        v = set()
        graph = defaultdict(list)
        
        for i, j in connections:
            graph[i] += [(j, True)]
            graph[j] += [(i, False)]
            
        q = deque([0])
        count = 0
        
        while q:
            cur = q.popleft()
            v.add(cur)
            
            for i, st in graph[cur]:
                if i not in v:
                    count += int(st)
                    q.append(i)
        return count