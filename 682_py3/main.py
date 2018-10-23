class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        s = []
        max_s = 0
        for i in ops:
            if i.isdigit() or i.startswith("-"):
                s.append(int(i))
                max_s += int(i)
            elif i == '+':
                if s and len(s) >= 2:
                    s.append(s[-1]+s[-2])
                    max_s += s[-1]
            elif i == "D":
                if s:
                    s.append(s[-1]*2)
                    max_s += s[-1]
            elif i == 'C':
                if s:
                    data = s.pop()
                    max_s -= data
        return max_s

print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]))

