class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        back = "0"
        for i in bin(n)[2:]:
            if back == i:
                return False
            back = i
        return True