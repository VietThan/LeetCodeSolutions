# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        iter1 = l1
        iter2 = l2
        
        head = ListNode(0)
        result = head
        
        carry = 0
        
        while iter1 or iter2 or carry:
            sum = carry
            if iter1:
                sum += iter1.val
                
            if iter2:
                sum += iter2.val
                
            carry, rem = divmod(sum, 10)
            head.next = ListNode(rem)
            
            head = head.next
            
            iter1 = iter1.next if iter1.next else None
            iter2 = iter2.next if iter2.next else None
        
        return result.next;

