
class Solution:
    def isValid(self, s: str) -> bool:

        ss = []

        for k in s:
            ss.append(k)

        #print(ss)

        for i in range(int(len(ss)/2)):
            #print(i)
            (l,r) = ss[(i*2)], ss[(i*2)+1]
            #print(l,r)
            #if l == '(' and r == ')' or l == '[' and r == ']' or l == '{' and r == '}':
            if (l,r) == ('(', ')') or (l,r) == ('[',']') or (l,r) == ('{','}'):
                #if i is (int(len(ss)/2)):
                return True

            else:
                return False



print(Solution().isValid("()[]{}"))



