class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return list(map(int, str(int("".join(map(str,digits))) + 1)))




print(Solution().plusOne([1,3,2,4]))