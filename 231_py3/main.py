class Solution:
    def isPowerOfTwo(self, num):
        """
        :type n: int
        :rtype: bool
        """
        if num == 1:
            return True

        data = bin(num)[2:]

        return data.startswith("10") and (data[2:].count("0") == len(data[2:]))