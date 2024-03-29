# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: list[int] , l2: list[int]) -> int:
        l1sum = 0
        l2sum = 0
        ans = []
        for count, value in enumerate(l1):
            if count == 0:
                l1sum = l1sum + value
            else:
                l1sum = l1sum + (10 ** count * value)

        for count, value in enumerate(l2):
            if count == 0:
                l2sum = l2sum + value
            else:
                l2sum = l2sum + (10 ** count * value)

        return l1sum + l2sum

print(Solution.addTwoNumbers([], (2,4,3), (5,6,4)))