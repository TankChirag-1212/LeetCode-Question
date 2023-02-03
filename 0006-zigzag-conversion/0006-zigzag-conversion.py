class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s

        sections = len(s) // (2*numRows - 2)
        numCols = sections*(numRows -1) + (numRows - 2)
        if numRows == 2:
            numCols = (len(s)// 2) + 1 
        
        matrix = [["0"]*numCols for _ in range(numRows)]
        currRow = 0
        currCol = 0
        currIndexOfs = 0

        while currIndexOfs < len(s):
            while (currRow < numRows and currIndexOfs < len(s)):
                matrix[currRow][currCol] = s[currIndexOfs]
                currRow += 1
                currIndexOfs += 1
            
            currRow -= 2
            currCol += 1

            # while (currRow > 0 and currIndexOfs < len(s)):
            while (currRow > 0 and currCol < numCols and currIndexOfs < len(s)):
                matrix[currRow][currCol] = s[currIndexOfs]
                currRow -= 1
                currCol += 1
                currIndexOfs += 1

        # print(f"{matrix} \n")
        answer = ""

        for row in range(len(matrix)):
            for i in range(len(matrix[row])):
                if matrix[row][i] != "0":
                    answer += matrix[row][i]
        return answer

