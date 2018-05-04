class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        data = {}
        for move in moves:
            data.setdefault(move,0)
            data[move]+=1
        return data.get("U") == data.get("D") and data.get("R") == data.get("L")