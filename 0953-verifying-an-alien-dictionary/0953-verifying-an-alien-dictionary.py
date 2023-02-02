class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        Hashmap = {}

        for i, value in enumerate(order):
            Hashmap[value] = i     
            
        for i in range(len(words)-1):
            currStr = words[i]
            nextStr = words[i+1]

            minLen = min(len(currStr), len(nextStr))

            if(minLen != len(currStr) and minLen == len(nextStr) and currStr.startswith(nextStr)):
                return False

            for j in range(minLen):
                if Hashmap[currStr[j]] > Hashmap[nextStr[j]]:
                    return False

                if Hashmap[currStr[j]] < Hashmap[nextStr[j]]:
                    break

        return True
