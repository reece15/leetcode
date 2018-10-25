class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        m = 0

        flag = False
        for i in nums:
            if i == 0:
                flag = True
            elif i > m:
                m = i
            res += i

        if not flag:
            return 0

        d = int((m + 1) * m / 2) - res
        if d:
            return d
        else:
            return m + 1