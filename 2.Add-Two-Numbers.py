#https://leetcode.com/problems/add-two-numbers
#Tried to make my python solution different from my cpp solution. Beats 92.5% runtime and 81.3% memory usage.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        anslist = ListNode(0)
        current = anslist
        carry = 0
        
        while l1 != None or l2 != None or carry != 0:
            if l1:
                val1 =  l1.val
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0
            
            carry = carry + val1 + val2 #add val1 and val2 to carry
            tempnode = ListNode(carry % 10) #create new node with first digit from sum
            carry = carry // 10 #assign new value to carry
            current.next = tempnode #move to next node
            current = tempnode #set pointer to next node
            #if l1 & l2 are not empty, then iterate through the next node. Else set next to None
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None

        return anslist.next
