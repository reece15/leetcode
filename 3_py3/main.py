class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        data_len = len(s)
        index = 0
        data_map = {}
        max_len=0
        point = 0
        while index < data_len:
            if s[index] in data_map and data_map[s[index]] >= point:
                point = data_map[s[index]]+1
            max_tmp = index - point + 1
            max_len = max(max_tmp, max_len)
            data_map[s[index]] = index
            index+=1
        if max_len==0:
            max_len=data_len
        return max_len
