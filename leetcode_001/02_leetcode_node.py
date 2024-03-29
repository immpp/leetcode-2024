from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def NodeMath(x):
            lsum = 0
            for count, value in enumerate(x):
                # print(count, value)
                if count == 0:
                    lsum = lsum + value
                else:
                    lsum = lsum + 10 ** count * value
            # print(lsum)
            return lsum

        asum = NodeMath(l1) + NodeMath(l2)
        ans = list((map(int,str(asum))))
        ans2 = list(reversed(ans))
        return ans2

print(Solution.addTwoNumbers([], [2, 4, 3], (5, 6, 4)))