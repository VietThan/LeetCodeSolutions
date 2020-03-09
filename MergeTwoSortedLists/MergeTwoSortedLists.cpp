/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* curr = head;
        
        while(l1 != nullptr && l2 != nullptr){
            // assign curr->next
            if(l1->val > l2->val){
                curr->next = l2;
                l2 = l2->next;
            } else {
                curr->next = l1;
                l1 = l1->next;
            }
            
            // advance curr
            curr = curr->next;
        }
        
        // at this point either l1 or l2 is nullptr
        // ir both is nullptr
        if (l1 == nullptr){
            curr->next = l2;
        }
        
        if (l2 == nullptr){
            curr->next = l1;
        }
        
        
        return head->next;
    }
};
