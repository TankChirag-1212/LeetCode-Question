class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        arr1 = []
        arr2 = []
        for i in s:
            arr1.append(s.index(i))
        for j in t:
            arr2.append(t.index(j))
        if arr1 == arr2:
            return True
        else:
            return False
        
        
