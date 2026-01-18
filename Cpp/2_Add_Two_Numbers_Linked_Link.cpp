/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* res = new ListNode(); 
        ListNode* current = res;
        ListNode* new_node;
        int carry = 0;

        while ((l1 != nullptr) || (l2 != nullptr)) {
            int sum = carry;
            if (l1) {sum += l1 -> val;} 
            if (l2) {sum += l2 -> val;}
            //int sum = (l1 -> val) + (l2 -> val) + carry;

            new_node = new ListNode(sum % 10);
            carry = sum / 10;

            current -> next = new_node;
            if (l1) {l1 = l1 -> next;} 
            if (l2) {l2 = l2 -> next;}
            current = current -> next;
        }
        /*
        if (l1 == nullptr and l2 != nullptr) {
            while (l2 != nullptr) {
                int sum = carry;
                if (l2) {sum += l2 -> val;}
                if (sum < 10) {
                    new_node = new ListNode(sum);
                    carry = 0;
                } else {
                    new_node = new ListNode(sum - 10);
                    carry = 1;
                }
                current -> next = new_node;
                l2 = l2 -> next;
                current = current -> next;
            }
        } else if (l2 == nullptr and l1 != nullptr) {
            while (l1 != nullptr) {
                int sum = carry;
                if (l1) {sum += l1 -> val;} 
                if (sum < 10) {
                    new_node = new ListNode(sum);
                    carry = 0;
                } else {
                    new_node = new ListNode(sum - 10);
                    carry = 1;
                }
                current -> next = new_node;
                l1 = l1 -> next;
                current = current -> next;
            }
        } */

        if (carry) {
            current -> next = new ListNode(carry);
        }

        return (res -> next);
    }
};