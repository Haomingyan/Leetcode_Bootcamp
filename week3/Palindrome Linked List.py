# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        self.front_pointer = head

        def recurssion_check(curr_node):
            if curr_node is not None:
                if not recurssion_check(curr_node.next):
                    return False
                if self.front_pointer.val != curr_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recurssion_check(head)
