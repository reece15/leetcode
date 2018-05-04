class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        # mapping = dict(zip([chr(i) for i in range(ord('a'), ord('z')+1,1)],a))
        
        mapping = {'a': '.-',
             'b': '-...',
             'c': '-.-.',
             'd': '-..',
             'e': '.',
             'f': '..-.',
             'g': '--.',
             'h': '....',
             'i': '..',
             'j': '.---',
             'k': '-.-',
             'l': '.-..',
             'm': '--',
             'n': '-.',
             'o': '---',
             'p': '.--.',
             'q': '--.-',
             'r': '.-.',
             's': '...',
             't': '-',
             'u': '..-',
             'v': '...-',
             'w': '.--',
             'x': '-..-',
             'y': '-.--',
             'z': '--..'}
        return len(set(map(lambda word: "".join((mapping[w] for w in word)), words)))