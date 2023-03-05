class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        count = flag = 0
        for i in range(time+1):
            if count < n and flag == 0:
                count += 1
            else:
                flag = 1
                count -= 1
                if count == 1:
                    flag = 0
        return count
    
# we keep track of the number we are passing pillow to using count and if the count is equal to n then we decrement the count and again increment when we reach the value of count as 1
# with the help of flag we keep track of incrimenting and decrimenting the count if count == n then we makes the flag 1 and decrement the count until count == 1
# then we change the flag to 0 again and continues the increment of count