class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        max_val = 2**31-1
        min_val = -2**31
        if min_val<=dividend <= max_val and min_val <= divisor <= max_val:

            flag_a = 1
            flag_b = 1
            if dividend<0:
                flag_a=0
                dividend = -dividend
            if divisor<0:
                flag_b = 0
                divisor = - divisor

            if flag_a^flag_b:
                step = -1
                if divisor == 1:
                    return -dividend
            else:
                if divisor==1:
                    return dividend if min_val<=dividend<=max_val else max_val
                step = 1

            index = 0
            while dividend>= divisor:
                block = divisor
                i = 0
                while dividend >= block:
                    dividend-=block
                    index += 1 << i
                    i+=1
                    block <<= 1
        else:
            return max_val

        return index if step == 1 else -index