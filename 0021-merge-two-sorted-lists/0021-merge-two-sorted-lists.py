# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        # Iterate while both lists are not empty
        while list1 and list2:
            # Compare values and append the smaller node to the merged list
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # Move the current pointer to the last node in the merged list
            current = current.next

        # If one of the lists is not empty, append the remaining nodes
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # The merged list starts from the next of the dummy node
        return dummy.next
