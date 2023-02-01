class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        def isValid(k):
            if len1 % k or len2 % k:      # condition gets true when we get the GCD of lengths of both strings
                return False
            n1 = len1//k          # only one "/"" gives the float value but "//" gives the int value as answer
            n2 = len2//k
            base = str1[:k]
            return str1 == n1*base and str2 == n2*base  # this condition is used because their may be multiple GCD but we need only one which is highest

        for i in range(min(len1,len2),0,-1):     #it runs the loop from minimum length to the 1 and value decreases after every iteration
            if isValid(i):
                return (str1[:i])
        return ""