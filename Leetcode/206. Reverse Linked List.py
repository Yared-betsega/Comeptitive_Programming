# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        temp = head
        while temp.next:
            prev = head
            head = temp.next 
            temp.next = temp.next.next
            head.next = prev
            
        return head