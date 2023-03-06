class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        numbers = []
        
        for i in range(1,2001):
            numbers.append(i)
            
        for i in range(len(arr)):
            numbers.remove(arr[i])
        print(numbers)   
        return numbers[k-1]