# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        currentNodeForList1 = list1;
        currentNodeForList2 = list2;
        head: ListNode = ListNode(0, None)
        curr: ListNode = head
        
        while (currentNodeForList1 and currentNodeForList2):
            if currentNodeForList1.val <= currentNodeForList2.val:
                curr.next = currentNodeForList1
                currentNodeForList1 = currentNodeForList1.next

            else:
                curr.next = currentNodeForList2
                currentNodeForList2 = currentNodeForList2.next

            curr = curr.next

        if (not currentNodeForList2):
            curr.next = currentNodeForList1
                

        if (not currentNodeForList1):
            curr.next = currentNodeForList2

        return head.next  






