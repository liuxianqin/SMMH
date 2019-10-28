/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {

        while(head !=null&&head.val ==val )

        {
//            ListNode retNode = head;
//            head = null;
//            retNode.next = head;
        ListNode delNode = head;               //为什么safadsfasfasdfasdfsadf
        head = head.next;
        delNode = null;
        }

        if(head == null)
            return null;

        ListNode prev = head;
        while(prev.next != null){
            if(prev.next.val == val){
                ListNode delNode = prev.next;
                prev.next = prev.next.next;
                delNode = null;                    //为什么 delNode.next = null
            }
            else
                prev = prev.next;
        }

        return head;
    }
}