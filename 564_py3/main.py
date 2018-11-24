#coding:utf-8

class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        num = int(n)



        # 得到最近回文
        c, index, t = self.get_part(n)
        # 在最近回文的左边从中间开始加1 和 减1
        l, l_index, l_t = self.next_part(c, index, t, 1)
        r, r_index, r_t = self.next_part(c, index, t, -1)

        # 相等时就会取最小的
        box = sorted([c, l, r], key=lambda x: int(x))

        return min(filter(lambda x: x!= n, box),key=lambda x: abs(int(x) - num))


    def next_part(self, n, s, t, add_sub):
        if not t:
            num = 10**s * add_sub
        else:
            if add_sub>0:
                num = 10**s * (11-int(n[s]))*add_sub
            else:
                num = 10**s* (int(n[s]) + 1) *add_sub

        res = str(num + int(n))
        return self.get_part(res)


    def brute_find(self, n):
        s = int(n)
        e = s

        while True:
            s-= 1
            if self.is_part(s):
                return str(s)
            e += 1
            if self.is_part(e):
                return str(e)

    def get_part(self, s):
        cnt = len(s)
        index = cnt//2
        if cnt % 2==0:
            return s[:index]+s[:index][::-1], index-1, True
        else:
            return s[:index+1] + s[:index][::-1], index, False


    def is_part(self, s):
        s = str(s)
        l = len(s)
        for i in range(l//2):
            if s[i] != s[l - i - 1]:
                return False
        return True


print(Solution().nearestPalindromic("120"))
exit()
for i in range(1,1000000):
    x = str(i)
    a = Solution().brute_find(x)
    b = Solution().nearestPalindromic(x)
    assert  a==b , (i,a,b)