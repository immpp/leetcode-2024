from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        pre2 = ""
        all_len = 0
        dict = {}
        count = 1
        for word in strs:
            print(len(strs))
            all_len = all_len + len(word)
            print(all_len)
            for letter in word:
                if letter in strs[0+count]:
                pre = pre + letter



        return pre


print(Solution().longestCommonPrefix(["flower","flow","flight"]))