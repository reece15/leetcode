		"""
		a = 3
        b = 5
        c = 15
        data = []
        for i in range(1, n+1, 1):
            s=None
            if i == c:
                s = "FizzBuzz"
                c += 15
                b += 5
                a += 3
            elif i == b:
                s = "Buzz"
                b += 5
            elif i == a:
                s = "Fizz"
                a += 3
            else:
                s = str(i)
            data.append(s)
        return data
		"""
		
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a = 3
        b = 5
        data = []
        for i in range(1, n+1, 1):
            s = ""
            if i == a:
                s += "Fizz"
                a += 3
            if i == b:
                s += "Buzz"
                b += 5
            if not s:
                s = str(i)
            data.append(s)
        return data