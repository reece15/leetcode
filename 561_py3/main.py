class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        data = sorted(nums)
        res = 0
        for i in range(0, len(nums), 2):
            res += min(data[i:i+2])

        return res


print(Solution().arrayPairSum([1,2,3,4]))