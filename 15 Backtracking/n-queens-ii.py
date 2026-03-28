class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_valid(board, row, col):
            for i in range(row):
                if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                    return False
            return True

        def place_queens(n, row, board, count):
            if row == n:
                return count + 1
            for col in range(n):
                if is_valid(board, row, col):
                    board[row] = col
                    count = place_queens(n, row + 1, board, count)
            return count

        board = [-1]*n
        return place_queens(n, 0, board, 0)
