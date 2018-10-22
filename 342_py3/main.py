class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        data = bin(num)[2:]

        return data.startswith("100") and (data[3:].count("0") % 2 == 0 and data[3:].count("1") == 0)


