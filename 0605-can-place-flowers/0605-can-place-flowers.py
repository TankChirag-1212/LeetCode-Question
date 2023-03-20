class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(n==0):
            return True;
        m = len(flowerbed)
        if(m==1 and flowerbed[0]==0 and n<=1):
            return True
        elif(m==1):
            return False
        canPlant = (flowerbed[0]==flowerbed[1]==0)
        
        for i in range(m-1):
            
            if(flowerbed[i]==0 and canPlant and flowerbed[i]==flowerbed[i+1]):
                n -= 1
                flowerbed[i] = 1
                canPlant = False
            else :
                if(flowerbed[i]==1):
                    canPlant = False
                elif(not canPlant):
                    canPlant = True
        
        if(flowerbed[m-2]==flowerbed[m-1] and flowerbed[m-1]==0):
            n -= 1
            
        return n<=0
                    
                