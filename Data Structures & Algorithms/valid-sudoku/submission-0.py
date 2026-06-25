class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowSet = set()
            for j in range(9):
                if (board[i][j] != '.'):
                    if board[i][j] in rowSet:
                        return False
                    else:
                        rowSet.add(board[i][j])    

                

        print('rowset')
        
        for i in range(9):
            colSet = set()
            for j in range(9):
                if (board[j][i] != '.'):
                    if board[j][i] in colSet:
                        return False
                    else:
                        colSet.add(board[j][i])

        print('colset')

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                miniSqSet = set()

                if board[i][j] != '.':
                    if board[i][j] not in miniSqSet:
                        miniSqSet.add(board[i][j])
                    else:
                        return False

                if board[i][j + 1] != '.':
                    if board[i][j + 1] not in miniSqSet:
                        miniSqSet.add(board[i][j + 1])
                    else:
                        return False

                if board[i][j + 2] != '.':
                    if board[i][j + 2] not in miniSqSet:
                        miniSqSet.add(board[i][j + 2])
                    else:
                        return False

                if board[i + 1][j] != '.':
                    if board[i + 1][j] not in miniSqSet:
                        miniSqSet.add(board[i + 1][j])
                    else:
                        return False

                if board[i + 2][j] != '.':
                    if board[i + 2][j] not in miniSqSet:
                        miniSqSet.add(board[i + 2][j])
                    else:
                        return False

                if board[i + 1][j + 1] != '.':
                    if board[i + 1][j + 1] not in miniSqSet:
                        miniSqSet.add(board[i + 1][j + 1])
                    else:
                        return False

                if board[i + 2][j + 2] != '.':
                    if board[i + 2][j + 2] not in miniSqSet:
                        miniSqSet.add(board[i + 2][j + 2])
                    else:
                        return False

        return True
        