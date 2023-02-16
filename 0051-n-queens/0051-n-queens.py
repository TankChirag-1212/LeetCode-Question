class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["...."] for _ in range(n)]
        ans = []
        col = set()
        rightDiago = set()
        LeftDiago = set()
        
        def backTrack(r,temp):
            if r == n:
                ans.append(temp)
                return

            for c in range(n):
                if c in col or (r+c) in rightDiago or (r-c) in LeftDiago:
                    continue
                col.add(c)
                rightDiago.add(r+c)
                LeftDiago.add(r-c)
                board[r] = ["." * c + "Q" + "." * (n-c-1)]
                
                backTrack(r+1, temp + board[r])

                col.remove(c)
                rightDiago.remove(r+c)
                LeftDiago.remove(r-c)
                board[r] = ["...."]
                
        backTrack(0,[])
        return(ans)

    
