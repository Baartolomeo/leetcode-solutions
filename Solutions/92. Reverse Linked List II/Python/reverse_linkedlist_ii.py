#Time complexity: O(n)
#Space complexity: O(n)

"""Description.

Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position
right, and return the reversed list.

Example:
    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]

"""

# Definition for singly-linked list.
class ListNode:
    """Node in Linked list"""
    def __init__(self, val=0, next=None):
        """
        :param val: value of node
        :param next: reference to next node in
                     linked list
        """
        self.val = val
        self.next = next

class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """Implementation of problem solution.

        :param head: array of nodes when first
                    element is a head
        :param left: left bound
        :param right: right bound
        :return: reversed linked list
        """
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
