class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ''' 
        list = [1,2,3,4]
        index_list = [0,1,2,3]
        
        use loop to get the index list, something like
        
        for i in range(len(list)):
        
        to reverse, notice that the last element is just the length of list, make a new list to store len(list)-1
        
        len(list) - 1
        4-1 = 3 -> 4, add to the new list in the first index (head)
        3-1 = 2 -> 3
        2-1 = 1 -> 2
        1-1 = 0 -> 1
        
        or, we could write it this way
        
        4-1 = 3
        4-2 = 2
        4-3 = 1
        4-4 = 0
        '''

        # org_list = [1, 2, 3, 4]
        # reversed_list = []
        # i = len(org_list)-1
        # while i > 0:
        #     reversed_list.append(org_list[i])
        #     i -=1

        ''' To use linked list
        flag the current node,
        flag the head of the node and reverse it
        the previous node becomes the current node, and the current node becomes the next node
        
        prev = None
        current = 1 -> 2 -> 3 -> 4 -> None
        next_node = 2 -> 3 -> 4 -> None
        
        Reverse the First Node (1):
            Update current.next to point to prev.
            (Now 1 points to None.)
            Move prev forward to current.
            (Now prev becomes 1.)
            Move current forward to next_node.
            (Now current becomes 2.)
        
            prev = 1 -> None
            current = 2 -> 3 -> 4 -> None
            next_node = 2 -> 3 -> 4 -> None
        
        Reverse the Second Node (2):
            Update current.next to point to prev.
            (Now 2 points to 1.)
            Move prev forward to current.
            (Now prev becomes 2.)
            Move current forward to next_node.
            (Now current becomes 3.)
        
            prev = 2 -> 1 -> None
            current = 3 -> 4 -> None
            next_node = 3 -> 4 -> None
        
        Full Example:
        Input: 1 -> 2 -> 3 -> 4 -> None
        Output: 4 -> 3 -> 2 -> 1 -> None
        
        Steps:
            1. Initial state: prev = None, current = 1 -> 2 -> 3 -> 4 -> None
            2. After processing 1:
                prev = 1 -> None, current = 2 -> 3 -> 4 -> None
            3. After processing 2:
                prev = 2 -> 1 -> None, current = 3 -> 4 -> None
            4. After processing 3:
                prev = 3 -> 2 -> 1 -> None, current = 4 -> None
            5. After processing 4:
                prev = 4 -> 3 -> 2 -> 1 -> None, current = None
            6. Return prev as the new head.

        
        '''
        prev = None
        current = head

        while current:
            next_node = current.next  # Save the next node
            print(f"Reversing Node {current.val}")  # Debugging

            current.next = prev  # Reverse the link
            prev = current  # Move prev to current
            current = next_node  # Move to the next node

            # Debugging
            print(f"Current: {current.val if current else None}, Prev: {prev.val}")

        return prev  # New head of the reversed list

    # helper function
    def create_linked_list(self, arr):
        head = ListNode(self, arr[0])
        current = head
        for val in self, arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def print_linked_list(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        print(result)

solution = Solution()

head = solution.create_linked_list([1,2,3,4])
reversed_head = solution.reverseList(head)
solution.print_linked_list(reversed_head)
