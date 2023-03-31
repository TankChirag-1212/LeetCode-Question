class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        
        '''      
        first we created 2d array which shows the total number of apples in the sub_grid
        e.g.[9,6,4,3,0]
            [7,5,3,2,0]
            [4,3,2,2,0]
            [3,2,1,1,0]
            [0,0,0,0,0]
        formula used to fill all the cells in this 3d array is --> prefix_sum[i][j] = cur_cell + right_grid + bottom_grid - bottom_right_grid
        '''
        row, col = len(pizza), len(pizza[0])
        prefix_sum = [[0 for j in range(col+1)] for i in range(row+1)]
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                cur_cell = 0
                if pizza[i][j] == 'A':
                    cur_cell = 1
                right_grid = prefix_sum[i][j+1]
                bottom_grid = prefix_sum[i+1][j]
                bottom_right_grid = prefix_sum[i+1][j+1]
                
                prefix_sum[i][j] = cur_cell + right_grid + bottom_grid - bottom_right_grid
        
        cache = {}      # memoization of answers
        def dp(cur_row, cur_col, k):
            
            if (cur_row, cur_col, k) in cache:
                return cache[(cur_row, cur_col, k)]
            
            if prefix_sum[cur_row][cur_col] == 0:  # base case 1
                return 0
            if k == 0:  # base case 2
                return 1
            ans = 0
            
#  checking all the possible cuts in the row
            for i in range(cur_row+1, row):
                if prefix_sum[cur_row][cur_col] - prefix_sum[i][cur_col] > 0:
                    ans += dp(i, cur_col, k-1)
#  checking all the possible cuts in the col
            for j in range(cur_col+1, col):
                if prefix_sum[cur_row][cur_col] - prefix_sum[cur_row][j] > 0:
                    ans += dp(cur_row, j, k-1)
                    
            cache[(cur_row, cur_col, k)] = ans
            return ans
        return dp(0,0,k-1) % (10**9 + 7)