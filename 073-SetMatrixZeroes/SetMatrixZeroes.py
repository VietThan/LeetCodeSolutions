class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # pulling matrix size
        rowCount = len(matrix)
        colCount = len(matrix[0])
        
        # flags for the zeroth row and col
        # because setting matrix[0][0] = 0
        # is confusing
        zeroRow = False
        zeroCol = False
        
        # check zero row
        for j in range(colCount):
            if matrix[0][j] == 0:
                zeroRow = True
        
        # check zero col
        for i in range(rowCount):
            if matrix[i][0] == 0:
                zeroCol = True
                
        # check remaining rows and cols
        for i in range(1, rowCount):
            for j in range(1, colCount):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        
        # iterate over 1..colCount columns:
        for j in range(1, colCount):
            if matrix[0][j] == 0:
                for i in range(1, rowCount):
                    matrix[i][j] = 0
                    
        # iterate over 1..rowCount rows:
        for i in range(1, rowCount):
            if matrix[i][0] == 0:
                for j in range(1, colCount):
                    matrix[i][j] = 0
        
        # iterate if for zero row
        if zeroRow:
            for j in range(colCount):
                matrix[0][j] = 0
                
        # iterate if for zero col
        if zeroCol:
            for i in range(rowCount):
                matrix[i][0] = 0