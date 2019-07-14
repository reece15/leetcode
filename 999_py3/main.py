class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        cnt = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":

                    for k in range(1, i + 1):
                        if board[i - k][j] == "B":
                            break
                        elif board[i - k][j] == "p":
                            cnt += 1
                            break

                    for k in range(i + 1, 8):
                        if board[k][j] == "B":
                            break
                        elif board[k][j] == "p":
                            cnt += 1
                            break

                    for k in range(1, j + 1):
                        if board[i][j - k] == "B":
                            break
                        elif board[i][j - k] == "p":
                            cnt += 1
                            break

                    for k in range(j + 1, 8):
                        if board[i][k] == "B":
                            break
                        elif board[i][k] == "p":
                            cnt += 1
                            break

                    break

        return cnt




