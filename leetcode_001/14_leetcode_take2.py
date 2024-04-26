from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        dict = {}
        dict2 = {}
        val = 0
        for word in strs:
            for count, letter in enumerate(word):
                if letter not in dict:
                    dict[letter] = 1
                    dict2[letter] = count
                else:
                    if dict2[letter] is count:
                        dict[letter] = dict[letter] + 1
        for k, v in dict.items():
            #print(k, v)
            if len(dict) == 1 and len(strs) < 2:
                pre = k
            elif v > 1 and v >= val:
                val = v
                pre = pre + k
            else: break
        print(dict)
        print(dict2)
        return pre


print(Solution().longestCommonPrefix(["aa","aa"]))