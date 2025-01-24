class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2:ListNode) -> ListNode:
        dum = ListNode()
        current = dum

        # new_list = []
        # i,j=0,0
        # left, right = 0
        # for i in range(len(list1)):
        #     for j in range(len(list2)):
        ''' Nested loop giving much more time complexity'''
        # while i < len(list1) and j <len(list2):
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # add the remaining of both
        # if i < len(list1):
        #     new_list.extend(list1[i:])
        # if j < len(list2):
        #     new_list.extend(list2[j:])
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dum.next

solution = Solution()
list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(3, ListNode(4, ListNode(5)))

print(solution.mergeTwoLists(list1, list2))