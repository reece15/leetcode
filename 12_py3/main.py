#coding:utf-8

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        mapping = [
            ['', 'M', 'MM', 'MMM'],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ]
        res = ""
        for index, i in enumerate([1000,100,10,1]):
            res += mapping[index][num//i]
            num = num % i

        return res


print(Solution().intToRoman(3))