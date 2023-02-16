class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        L = len(p)
        dict_s = {}
        dict_p = {}
        ans = []
        
        if L > len(s):
            return []
        for i in set(s+p):
            dict_s[i] = 0
            dict_p[i] = 0
        
        for i in range(L):
            dict_p[p[i]] += 1
            dict_s[s[i]] += 1
        if dict_p == dict_s:
            ans.append(L-1-i)
                
        j = 0
        for i in range(L,len(s)):
            dict_s[s[j]] -= 1
            j += 1
            dict_s[s[i]] += 1
            if dict_p == dict_s:
                ans.append(abs(L-1-i))
        return ans
            
        
