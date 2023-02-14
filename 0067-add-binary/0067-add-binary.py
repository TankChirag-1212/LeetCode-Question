class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b)< len(a):
            x = len(a) - len(b)
            b = "0"*x + b
        if len(a)< len(b):
            x = len(b) - len(a)
            a = "0"*x + a
        n = len(a)
        carry = False
        ans = ""

        for i in range(n-1,-1,-1):
            n1 = 0
            if carry:
                n1 = 1
            if int(a[i])+int(b[i])+ n1 == 0:
                ans = "0" + ans
            if int(a[i])+int(b[i])+ n1 == 1 and n1 == 0:
                ans = "1" + ans
            if int(a[i])+int(b[i])+ n1 == 1 and n1 == 1:
                carry = False
                ans = "1" + ans
            if int(a[i])+int(b[i])+ n1 == 2 and n1 == 1:
                ans = "0" + ans
            if int(a[i])+int(b[i])+n1 == 3:
                carry = True
                ans = "1" + ans
            if int(a[i])+int(b[i])+n1 == 2 and n1 == 0:
                carry = True
                ans = "0" + ans
        if carry:
            ans = "1" + ans
        return ans if(ans != "") else "0"