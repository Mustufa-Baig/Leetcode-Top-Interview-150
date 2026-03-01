class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        
        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if (i == r and j == c) or i < 0 or i >= m or j < 0 or j >= n:
                            continue
                        if abs(board[i][j]) == 1:
                            live_neighbors += 1
                
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2
        
        for r in range(m):
            for c in range(n):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
