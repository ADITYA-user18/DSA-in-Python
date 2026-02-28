class Solution(object):
    def mergeTwoLists(self, list1, list2):

        head1 = list1
        head2 = list2
        new_LinkedList = ListNode(0)
        dummy = new_LinkedList

        while head1 and head2:
            if head1.val <= head2.val:
                new_LinkedList.next = head1
                head1 = head1.next
            else:
                new_LinkedList.next = head2
                head2 = head2.next
            
            new_LinkedList = new_LinkedList.next

        if head1:
            new_LinkedList.next = head1
        else:
            new_LinkedList.next = head2
        
        return dummy.next