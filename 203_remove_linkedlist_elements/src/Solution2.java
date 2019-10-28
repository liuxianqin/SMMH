/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution2 {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummyhead = new ListNode(-1);
        dummyhead.next = head;


        ListNode prev = dummyhead;              //头是从dummyHead开始的
        while(prev.next != null){
            if(prev.next.val == val){
                ListNode delNode = prev.next;
                prev.next = prev.next.next;
                delNode.next = null;
            }
            else{
                prev = prev.next;
            }
        }
//        return head;
        return dummyhead.next;
    }
}