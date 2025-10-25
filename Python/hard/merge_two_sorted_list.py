#Title: Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy.next

# Helper function to print linked list
def printList(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))

# Helper function to create linked list from Python list
def createList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example usage
if __name__ == "__main__":
    l1 = createList([1, 2, 4])
    l2 = createList([1, 3, 4])
    merged = mergeTwoLists(l1, l2)
    printList(merged)
    
    
    from scripts.utils import log_and_update
    log_and_update("Python/hard/merge_two_sorted_list.py") 