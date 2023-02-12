class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        hashMap = defaultdict(list)      # it creats the empty hashMap
        
        for src,dst in roads:               # it will creat the dictionary or say hashmap to store all the posible routes of one node can take
            hashMap[src].append(dst)
            hashMap[dst].append(src)
            
            
        def dfs(node,parent):
            nonlocal fuel             # fuel variable is global variable
            passengers = 0
            
            for child in hashMap[node]:   # it iterates for every child of the current node
                if child != parent:
                    p = dfs(child,node)     # recursive function which continues until one branch in tree ends
                    passengers += p          # number of childs one particular node have
                    fuel += int(ceil(p/seats))       # it gives the number of cars== fuel requires to get the child nodes to the current node say 5 child nodes with 2 seats then ceil(5/2)=3 cars requires
            return passengers+1
        fuel = 0
        dfs(0,-1)
        return fuel