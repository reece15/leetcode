class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
            
        return map(lambda y: [int(not i)  for i in y], map(lambda x: x[::-1],A))