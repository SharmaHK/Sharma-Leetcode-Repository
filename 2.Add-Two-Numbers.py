# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mult = 1
        ans = 0
        for i in range(2):
            ans += (l1.val * mult)
            #l1.val = l1.next
            mult *= 10
            print(mult)
        print(mult)
        return l1
