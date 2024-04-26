

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #return True if str(x) == str(x)[::-1] else False
        #refactor
        return str(x) == str(x)[::-1]






print(Solution().isPalindrome(8998))