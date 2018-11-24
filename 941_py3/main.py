class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        x = len(A)
        if x < 3:
            return False

        last = A[0]
        start_up = 0
        start_down = 0
        find_max = 0
        for i in A[1:]:
            if i > last:
                if start_down:
                    return False
                last = i
                start_up = 1
            elif i < last:
                if not find_max:
                    start_down = 1
                    find_max = 1
                if not start_up or not start_down:
                    return False
                last = i

            else:
                return False
        return bool(start_down and start_down)