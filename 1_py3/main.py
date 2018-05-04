class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = {}
        for index, i in enumerate(nums):
            for j_index, j in enumerate(nums[index+1:]):
                if i+j == target:
                    return index, index+j_index+1
