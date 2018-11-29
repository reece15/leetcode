#coding:utf-8

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x,next):
        self.val = x
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        s = head
        back = head

        now = self.move_to_N(head, n)
        if not now.next:
            return head.next

        last = back
        while  now.next:
            last = back
            back = back.next
            now = now.next
        last.next = back.next
        return s

    def show(self, head):
        while head:
            print(head.val,end="")
            head=head.next
        print()

    def move_to_N(self,  head, N):
        index = 1
        while index < N:
            head = head.next
            index += 1
        return head

print(Solution().removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, None))), 2))