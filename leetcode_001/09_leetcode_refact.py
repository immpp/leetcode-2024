#given x return true if x is a palindrome

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        lstr = list(str(x))
        rev_x = 0
        for count, num in enumerate(lstr):
            rev_x = rev_x + 10 ** int(count) * int(num)
        if x == rev_x: return True
        else: return False



print(Solution().isPalindrome(8908))