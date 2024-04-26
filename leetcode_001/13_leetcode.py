# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        year = 0
        for count, value in enumerate(s):
            if count < len(s)-1:
                if roman[s[count]] >= roman[s[count+1]]:
                    year = year + roman[value]
                else: year = year - roman[value]
            else: year = year + roman[value]
        return year



print(Solution().romanToInt('MCMXCIV'))
