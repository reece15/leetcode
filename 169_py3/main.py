# coding:utf-8

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        return Counter(nums).most_common()[0][0]




print(Solution().majorityElement([1,1,2,3,4,4,4,4,4,4,4]))