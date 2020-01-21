/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode current = head ;
        
        while (l1 != null & l2 !=null ){
            if (l1.val < l2.val){
                current.next = new ListNode(l1.val);
                l1 = l1.next;                
            }
            else{
                current.next = new ListNode(l2.val);
                l2 = l2.next;                       
                
            }
            current = current.next;
            
        }
        
        current.next  = l1!=null ? l1 : l2;   
       
        return head.next;        
    }
}