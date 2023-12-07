class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Traverse the linked list to find its length
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Calculate the position of the node to be removed from the beginning
        position_to_remove = length - n + 1

        # If the node to be removed is the first node
        if position_to_remove == 1:
            return head.next

        # Traverse the list again to the node just before the one to be removed
        current = head
        for _ in range(position_to_remove - 2):
            current = current.next

        # Adjust pointers to skip the node to be removed
        current.next = current.next.next

        return head
