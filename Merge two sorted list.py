from Palindrome import solution


class Solution(object):
    def mergeTwoLists(self, list1, list2):

        new_list = []
        i,j=0,0
        # left, right = 0
        # for i in range(len(list1)):
        #     for j in range(len(list2)):
        ''' Nested loop giving much more time complexity'''
        while i < len(list1) and j <len(list2):
            if list1[i] <= list2[j]:
                new_list.append(list1[i])
                i +=1
            else:
                new_list.append(list2[j])
                j +=1
        # add the remaining of both
        if i < len(list1):
            new_list.extend(list1[i:])
        if j < len(list2):
            new_list.extend(list2[j:])

        return new_list


solution = Solution()
print(solution.mergeTwoLists([1,2,3],[3,4,5]))


        # list1[0] = 1
        # list2[0] = 3
        #
        # add 1 to the new list
        #
        # list1[0] = 2
        # list2[0] = 4
        #
        # add 1,2 to the new list
        #
        # list1[0] = 3
        # list2[0] = 5
        #
        # add 1,2,3 to the new list
        #
        # the remaining element is 3,4,5. Add those elements to the rest of the new list