class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        
        self.mapping = {}
        a = 0
        for k in range(len(nums)):
            a += self.nums[k]
            self.mapping[k]=a
           

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i== 0:
            return self.mapping[j]
        return self.mapping[j] - self.mapping[i-1]  # a[j] -a[i-1] = a[i,j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)