#coding:utf-8

class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        index = 0
        for i in zip(*A):
            last = i[0]


            for j in i[1:]:
                if j <= last:
                    index += 1
                    break
                last = j



        return index

print(Solution().minDeletionSize(["a","b"]))

