/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode iter1 = l1;
        ListNode iter2 = l2;
        
        ListNode head = new ListNode(0);
        ListNode result = head;
        
        int carry = 0;
        
        while(l1 != null || l2 != null || carry != 0){
            int sum = ((l1 != null) ? l1.val : 0) + ((l2 != null) ? l2.val : 0) + carry;
            head.next = new ListNode(sum % 10);
            carry = sum / 10;
            head = head.next;
            
            l1 = (l1 != null) ? l1.next : l1;
            l2 = (l2 != null) ? l2.next : l2;
        }
        
        return result.next;
        
        
        
    }
}
