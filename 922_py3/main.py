class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        a = []
        b = []
        for i in A:
            if i % 2 == 0:
                a.append(i)
            else:
                b.append(i)
        c = []
        for x, y in zip(a, b):
            c += [x, y]
        return c