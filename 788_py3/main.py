class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        data_set = {"2","5","6","9"}

        b = {"0", "1", "8"}

        cnt = 0
        for i in range(1, N+1):
            flag1 = False
            flag2 = True
            for j in str(i):
                if j in data_set:
                    flag1 = True
                else:
                    if j not in b:
                        flag2 = False
                        break

            if flag1 and flag2:
                cnt += 1

        return cnt