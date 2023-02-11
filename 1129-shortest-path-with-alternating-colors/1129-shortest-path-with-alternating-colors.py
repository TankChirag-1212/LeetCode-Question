class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = collections.defaultdict(list)
        blue = collections.defaultdict(list)
        
        for src,dst in redEdges:
            red[src].append(dst)
        for src,dst in blueEdges:
            blue[src].append(dst)
            
        q = deque()
        ans = [-1 for _ in range(n)]
        q.append([0,0,None])  # append[node, length, prev_edge_color]   # it means we have visited the node 0
        visited = set()
        visited.add((0,None))   # to reach the node 0 there is no path so its 0 and color is none
        
        while q:
            node,length, prev_edge_color = q.popleft()      # it returns the detail of previously visited node
            if ans[node] == -1:
                ans[node] = length         # it updates the ans[] for the previously visited node
                
            if prev_edge_color != "Red":        # it checks if the previous edge was red or not
                for neighbor in red[node]:        # it checks if we can go to the next node or not
                    if (neighbor,"Red") not in visited:       # it checks if we visited the node in past, we are at right now
                        visited.add((neighbor, "Red"))
                        q.append([neighbor,length + 1,"Red"])     # if not it appends the details in queue and mark the node as visited in visited set{}
                        
            if prev_edge_color != "Blue":
                for neighbor in blue[node]:
                    if (neighbor,"Blue") not in visited:
                        visited.add((neighbor, "Blue"))
                        q.append([neighbor,length + 1,"Blue"])
                        
        return ans