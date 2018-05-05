class Solution:
    q_mapping = {'q', 'w','e','r','t','y','u','i','o','p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'}
    a_mapping = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'}
    z_mapping = {'z', 'x', 'c', 'v', 'b', 'n', 'm','Z', 'X', 'C', 'V', 'B', 'N', 'M'}
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        
        
        
        return list(filter(lambda word:  len(set((self.word_where(w) for w in word))) == 1, words))
        
    def word_where(self, word):
        if word in self.q_mapping:
            return 1
        elif word in self.a_mapping:
            return 0
        elif word in self.z_mapping:
            return -1
        else:
            return -2