class Solution(object):
    def isValidSudoku(self, board):

        '''
        :param board:
        :return: boolean
        '''

        for column in range(9):
            seen = set()
            for index in range(9):
                if board[index][column] == '.':
                    continue
                if board[index][column] in seen:
                    return False

                seen.add(board[index][column])

        for row in range(9):
            seen = set()
            for index in range(9):
                if board[row][index] == '.':
                    continue
                if board[row][index] in seen:
                    return False
                seen.add(board[row][index])


        # for 3*3 grid
        for grid in range(9):
            seen = set()
            # 3*3 is a matrix, so...
            for c in range(3):
                for r in range(3):
                    col = (grid //3) * 3 + c
                    row = (grid % 3) * 3 + r
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True

solution = Solution()
print(solution.isValidSudoku([
    ["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))

