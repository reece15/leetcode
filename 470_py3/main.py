
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

def rand7():
    import random

    return random.randint(0,7)

class Solution:
    data = list(range(10))
    def rand10(self):
        """
        :rtype: int
        """
        d = 0
        x = 0
        for i in range(10):
            d+= rand7()
            x += self.data[d%10]

        return x%10+1



def check(N):

    res = {}
    for i in range(N):
        d = Solution().rand10()
        if not res.get(d):
            res[d] = 0
        res[d]+=1
    return res

print(check(100000))