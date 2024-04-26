
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        dict = {}
        for word in strs:
            for letter in word:
                print(letter)
                if letter not in dict:
                    dict[letter] = 1
                else:
                    dict[letter] = dict[letter] + 1
        print(dict)
        print(max(dict, key=dict.get))
        return pre


print(Solution().longestCommonPrefix(["flower","flow","flight"]))

#print(Solution().longestCommonPrefix("flower","flow","flight"))