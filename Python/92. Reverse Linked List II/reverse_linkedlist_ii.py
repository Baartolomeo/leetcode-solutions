#Time complexity: O(n)
#Space complexity: O(n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current_node = root = head
        is_left_node = lambda x: x == left
        is_right_node = lambda x: x == right
        left_prev_node = None
        right_next_node = None
        reverse_last_node = None
        counter = 1
        while current_node and not is_left_node(counter):
            left_prev_node = current_node
            current_node = current_node.next
            counter += 1
        new_node = reverse_last_node = current_node
        while current_node:
            if is_right_node(counter):
                right_next_node = current_node.next
                break
            new_node = ListNode(val=current_node.next.val, next=new_node)
            current_node = current_node.next
            counter += 1
        if left_prev_node:
            left_prev_node.next = new_node
        else:
            root = new_node
        if reverse_last_node:
            reverse_last_node.next = right_next_node
        return root
