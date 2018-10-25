class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        n = 0

        for i in nums:
            if i == 1:
                n += 1
            else:
                n = 0
            if n > m:
                m = n

        return m