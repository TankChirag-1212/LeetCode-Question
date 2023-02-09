
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        wordMap = collections.defaultdict(set)

        for word in ideas:
            wordMap[word[0]].add(word[1:])    # it creates the dictionary with first char of each word in ideas as key and the suffix of it as a value.
        
        
        ans = 0
        for char1 in wordMap:     # char1 in wordmap means the key in the dictionary we created
            for char2 in wordMap:   # char2 in wordmap means the next key in the dictionary
                if char1 == char2:    # we don't want to repeat the same characters 
                    continue
                intersect = 0
                for w in wordMap[char1]:    # w in wordMap[char1] is refers to the first suffix made using the key(char1)
                    if w in wordMap[char2]:
                        intersect += 1           # if we found w(suffix) in set of both the char then we found an intersection among to set
                
                distinct1 = len(wordMap[char1]) - intersect     # this gives only the distinct suffix from the set of both the characters
                distinct2 = len(wordMap[char2]) - intersect

                ans += distinct1 * distinct2      # it gives the count of pair we can form using those different suffixes we get

        return ans