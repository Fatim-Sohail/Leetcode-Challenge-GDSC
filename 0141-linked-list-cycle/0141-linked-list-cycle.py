class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Initialize two pointers, slow and fast
        slow = head
        fast = head

        # Iterate until either the fast pointer reaches the end or there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If there is a cycle, the pointers will eventually meet
            if slow == fast:
                return True

        return False # No cycle found

