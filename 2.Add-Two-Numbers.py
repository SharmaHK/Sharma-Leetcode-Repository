# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def iterateList(l1: Optional[ListNode]):
        len = 0

        while l1.next != NULL:
            len +=1

        return len

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mult = 1
        anslist = Optional[ListNode]
        anslist = l2
        ans = 0

        len = 1
        while l1.next != None:
            len +=1
            l1 = l1.next
        print("length: ",len)

        for i in range(len):
            ans += (l1.val * mult)
            l1 = l1.next
            mult *= 10
            print(ans)


        return anslist
