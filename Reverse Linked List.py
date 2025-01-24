class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ''' 
        list = [1,2,3,4]
        index_list = [0,1,2,3]
        
        use loop to get the index list,
        something like
        
        for i in range(len(list)):
        
        to reverse, notice that the last element is just the length of list, 
        make a new list to store len(list)-1 
        
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
        
        
        '''


