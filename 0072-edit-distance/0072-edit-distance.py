class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")]*(len(word2)+1) for _ in range(len(word1) + 1)]
        
        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1) - i
        
        for i in range(len(word1)-1 , -1 , -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
#                                      insert       delete      replace
                    dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])
                    
        return dp[0][0]
    
# we use DP with memoization to store the values of every operations at each step
# first we build 2d array as a DP table then we fill the cells with infinity value
# we replace the value as we go further in solving the problem
# we create the extra column and row at the end as a base case then we fill the table starting from bottom and reaching to the top
# then we iterate the word2 string and check the characters in word1 and do the operations 
# in simple we check the down, right and diagonal values in the table of the current cell and we add the minimum value to the current cell.
# we do this untill all the values are filled in table and return the value of 1st cell in the 1st column and 1st row of the table.
