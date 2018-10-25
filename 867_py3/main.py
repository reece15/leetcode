class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        1 2 3
        4 5 6

        1 4

        2 5

        3 6

        """

        l = len(A[0])
        a = []
        for j in range(l):
            b = []
            for i in range(len(A)):
                b.append(A[i][j])
            a.append(b)
        return a