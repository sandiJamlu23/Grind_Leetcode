from code import interact
from sys import intern


class Solution(object):
    def intersection(self, num1, num2):
        '''
        Input: nums1 = [1,2,2,1],
        nums2 = [2,1,2]

        sort both list
        nums 1 = [1,1,2,2]
        nums 2 = [1,2,2]

        store the intersection result in an array.

        we need to loop through the first list, and compare it to the second list
        if the element in the first list equal to element in the second list, add that to the result

        if the element is already in the list ( a duplicate), ignore it.

        '''
        num1.sort()
        num2.sort()
        intresect_res = []
        # to check if the number is already in the result, use a dummy variable
        # intersect_set = set()
        # for num in num1:
        #     if num in num2:
        #         intersect_set.add(num)
        #
        # return list(intersect_set)

        for num in num1:
            if num in num2 and num1 in num2:
                intresect_res.append(num)

        return intresect_res


solution = Solution()
print(solution.intersection([1,2,2,1], [2,1,2]))
