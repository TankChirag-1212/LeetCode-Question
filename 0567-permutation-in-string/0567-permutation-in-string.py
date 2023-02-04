class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic_s1 = {}          # using dictionary to store the frequencies of elemnts in strings
        dic_s2 = {}
        L = len(s1)
        
        if L > len(s2):    #if s1 > s2 return false
            return False
        
        for i in set(s1+s2):
            dic_s1[i] = 0
            dic_s2[i] = 0
            
        for i in s1:
            dic_s1[i] += 1         #number frequencies updated in the dictionary 
        for i in range(L):
            dic_s2[s2[i]] += 1      # in dic_s2 only those elements are updated who matches the index of s1
        
        if dic_s1 == dic_s2:
            return True
        
        j = 0
        for i in range(L,len(s2)):    # this for loop shifts the window by element to the right side i.e. first element in s2
            dic_s2[s2[j]] -= 1
            j +=1
            dic_s2[s2[i]] += 1     # just next element of the last element in s2 in updated
            # print(dic_s2)
            if dic_s2 == dic_s1:
                   return True
        return False
            