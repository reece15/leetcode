class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        return str(int(bin(int(str(a),2) + int(str(b), 2))[2:]))



print(Solution().addBinary(11,1))