# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        tail=head
        carry=0

        while not(l1==None and l2==None and carry==0):
            d1= l1.val if l1!=None else 0
            d2= l2.val if l2!=None else 0
            
            num=d1+d2+carry
            carry=num//10
            tail.next=ListNode(num%10)
            tail=tail.next
            
            l1=l1.next if l1!=None else None
            l2=l2.next if l2!=None else None
            
        return head.next

