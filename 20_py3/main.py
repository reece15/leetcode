class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        mapping = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

        for i in s:
            if i in mapping:
                if not stack:
                    return False
                d = stack.pop()
                if mapping[i] != d:
                    return False
            else:
                stack.append(i)


        return not stack