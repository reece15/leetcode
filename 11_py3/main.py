#coding:utf-8

class Solution:
    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        from itertools import combinations

        max_val = 0
        for i in combinations(enumerate(height), 2):
            val = abs(i[0][0]-i[1][0])*min([i[0][1], i[1][1]])
            if val > max_val:
                max_val = val

        return max_val

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i = 0
        j = len(height) - 1
        max_val = 0
        while i < j:

            if height[i] < height[j]:
                h = height[j]
                j-=1
            else:
                h = height[i]
                i+=1
            max_val = max(max_val, (j-i)*h)
        return max_val


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))