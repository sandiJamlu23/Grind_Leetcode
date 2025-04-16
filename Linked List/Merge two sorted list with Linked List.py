from ctypes import c_uint


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1:ListNode, list2: ListNode)->ListNode:
        '''
        l1 = [1,2,3]
        l2 = [2,3,4]

        merge = [1,2,2,3,4]

        i,j = 0 -> 1 vs 2, keep 1
        merged_list = 1
                    2 vs 2, keep 2
        merged_list = 1,2
                    3 vs 2, keep 2
        merged_list = 1,2,2, list1 is empty. quit the loop

        left_over 3,3,4
        '''

        # check if the list is empty
        if not list1:
            return list2
        if not list2:
            return list1

        # initiate the head and the current node
        head = None
        current = None

        # which is supposed to be the head?
        if list1.val <= list2.val:
            head = list1
            # work with the next node
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        # the head is now a current node
        current = head

        # merging
        while list1 and list2:
            if list1.val <= list2.val:
                # work with the next node in list1
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # add the remaining element
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return head
    def print(self, node: ListNode):
        while node:
            print(node.val, end='->')
            node = node.next
        print("None")


solution = Solution()
list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(3, ListNode(4, ListNode(5)))

merged = solution.mergeTwoLists(list1, list2)
solution.print(merged)