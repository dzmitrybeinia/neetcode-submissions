class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        duplicates = defaultdict(set)
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                row_key = "r" + str(i)
                if board[i][j] in duplicates[row_key]:
                    return False
                else:
                    duplicates[row_key].add(board[i][j])
                col_key = "c" + str(j)
                if board[i][j] in duplicates[col_key]:
                    return False
                else:
                    duplicates[col_key].add(board[i][j])
                sq_key = "s" + str(i // 3) + "," + str(j // 3)
                if board[i][j] in duplicates[sq_key]:
                    return False
                else:
                    duplicates[sq_key].add(board[i][j])
        return True