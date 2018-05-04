#coding:utf-8

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return len(list(filter(lambda x: x, ( s == j for s in  S for j in J))))
        #return sum(1 for i in (s == j for s in  S for j in J) if i)
