class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        col_len = len(matrix)
        row_len = len(matrix[0])

        for i in range(col_len):
            
            if target >= matrix[i][0] and target <= matrix[i][row_len - 1]:
                s = 0
                e = row_len - 1

                while(s <= e):
                    m = s + (e - s) //2

                    if matrix[i][m] == target:
                        return True
                    elif target < matrix[i][m]:
                        e = m - 1
                    else:
                        s = m + 1

        return False 





            