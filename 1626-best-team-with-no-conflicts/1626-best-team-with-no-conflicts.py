class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i], ages[i]]for i in range(len(scores))]    # pairs stores the list of pairs of respective players score and age like ... [[2,1],[5,2],[3,1],[6,1]]
        pairs.sort()
        dp = [pairs[i][0]for i in range(len(pairs))]         # it stores all the scores of all players like....[2,5,3,6]

        for i in range(len(pairs)):
            maxScore, maxAge = pairs[i]         # it stores the value of maximum Score and Age up unitll now
            for j in range(i):
                score, age = pairs[j]             # it stores the score and age of particualr player 
                if maxAge >= age:
                    dp[i] = max(dp[i] , maxScore+dp[j])       # it updates the dp variable if new player is considered
        return (max(dp))