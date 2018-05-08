class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        if not str:
            return 0
        str = str.lstrip()
        
        dataSet = {'+', '-','0', '1', '2','3','4','5','6','7','8','9'}
        if not str or str[0] not in dataSet:
            return 0
        
        s = []
        start = 0
        
        if str[0] == "-":
            s.append("-")
            start = 1
        
        if str[0] == "+":
            start = 1
            
        
        flag = False
        for i in range(start, len(str)):
            if str[i] != '-' and str[i] != '+' and str[i] in dataSet:
                if not flag and str[i] != '0':
                    flag = True
                if flag:
                    s.append(str[i])
            else:
                break
        try:
            res = int("".join(s), 10)
        except:
            return 0
        if res > 2147483647:
            return 2147483647
        elif res < -2147483648:
            return -2147483648
        
        return res