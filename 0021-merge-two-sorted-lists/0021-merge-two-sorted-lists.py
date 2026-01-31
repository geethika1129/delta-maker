# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a=list1
        b=list2
        nhead=ListNode(None)
        dummy=nhead
        while a and b:
            if a.val<b.val:
                dummy.next=a
                a=a.next
            else:
                dummy.next=b
                b=b.next
            dummy=dummy.next
        if a:
            dummy.next=a
        if b:
            dummy.next=b
        return nhead.next
        