class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = num[::-1]
        i = 0
        while k:
            digit = k % 10
            if i < len(num):
                num[i] += digit
            else:
                num.append(digit)

            carry = num[i] // 10
            num[i] = num[i] % 10

            k = k//10
            k += carry
            i += 1
            
        return num[::-1]
    
# ANOTHER BASIC APPROACH

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans=[]
        a = num[0]
        
        for i in range(1,len(num)):
            a = a*10 + num[i]
        a = a+k
        
        for i in str(a):
            ans.append(int(i))
            
        return ans
