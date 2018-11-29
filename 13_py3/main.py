class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = [
            ['', 'M', 'MM', 'MMM'],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ]

        res = ""
        for index, i in enumerate(mapping):
            cnt = len(i)
            for j in range(cnt):
                x = cnt - j - 1
                if s.startswith(i[x]):
                    s = s[len(i[x]):]
                    res += str(x)
                    break
        return int(res)
