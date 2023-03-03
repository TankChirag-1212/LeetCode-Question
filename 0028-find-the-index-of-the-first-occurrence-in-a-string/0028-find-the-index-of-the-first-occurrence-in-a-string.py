class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        i,j = 0, n-1
        
        while j < h:
            if haystack[i:j+1] == needle:
                return i
            else:
                i += 1
                j += 1
        return -1