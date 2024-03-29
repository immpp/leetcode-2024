# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: list[int], l2: list[int]) -> list[int]:
        dict1 = {}
        dict2 = {}
        dict3 = {}
        ans = []

        for count, value in enumerate(l1):
            dict1[count] = value
        for count, value in enumerate(l2):
            dict2[count] = value

        for x in dict1:
            dict3[x] = dict2[x] + dict1[x]
            if dict3[x] >= 10:
                dict3[x] = 0
                dict1[x + 1] = dict1[x + 1] + 1

        for x in dict3:
            ans.append(dict3[x])

        return ans


print(Solution.addTwoNumbers([], (2,4,3), (5,6,4)))