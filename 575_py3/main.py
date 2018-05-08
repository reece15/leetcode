class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        num = len(candies)//2
        mm = {}
        mm_size = 0
        dd = {}
        dd_size = 0
        
        for i in candies:
            if mm.get(i) is None:
                mm[i] = 1
                mm_size += 1
                if mm_size == num:
                    return num
            else:
                dd[i] = 1
                dd_size += 1
        
        if dd_size > mm_size:
            return mm_size
        # mm_size > dd_size
        return mm_size - (num - dd_size)