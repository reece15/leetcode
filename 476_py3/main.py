class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = num
        num_xor = 0
        while tmp:
            tmp>>=1
            num_xor <<= 1
            num_xor += 1

        return num ^ num_xor