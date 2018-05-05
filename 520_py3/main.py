class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
#         if word[0] >= 'a':
#             return self.all_lower(word)
#         else:
#             if len(word) > 1:
#                 if word[1] >= 'a':
#                     return self.all_lower(word[1:])
#                 else:
#                     return self.all_upper(word[1:])
#             else:
#                 return True
            
#     def all_lower(self, word):
#         return all((w >= 'a' for w in word))
    
#     def all_upper(self, word):
#         return all((w <= 'Z' for w in word))
        return word.isupper() or word.islower() or word.istitle()