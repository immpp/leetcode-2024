from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        pre2 = ""
        pre3 = ""
        dict = {}
        for word in strs:
            for letter in word:
                if letter not in pre:
                    pre = pre + letter
                else: pre2 = pre2 + letter

        print(pre)
        print(pre2)
        for letter2 in pre2:
            print(pre2.count(letter2))

        return pre


print(Solution().longestCommonPrefix(["flower","flow","flight"]))