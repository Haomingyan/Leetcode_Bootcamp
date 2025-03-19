# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        if not head.next:
            return head
        stack = []
        curr = head
        while curr is not None:
            stack.append(curr)
            curr = curr.next

        curr = head
        for i in range(len(stack)//2):
            temp = curr.next
            reverse_node = stack.pop()
            curr.next = reverse_node
            reverse_node.next = temp
            curr = temp
        curr.next = None
        
        
