class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."]*n for _ in range(n)]
        count = [0]
        col = set()
        r_Diag = set()
        l_Diag = set()

        def backTrack(r):
            if r == n:
                count[0] += 1
                return

            for c in range(n):
                if c in col or (r+c) in r_Diag or (r-c) in l_Diag:
                    continue

                col.add(c)
                r_Diag.add(r+c)
                l_Diag.add(r-c)
                board[r][c] = "Q"

                backTrack(r+1)

                col.remove(c)
                r_Diag.remove(r+c)
                l_Diag.remove(r-c)
                board[r][c] = "."
                
        backTrack(0)
        return count[0]
