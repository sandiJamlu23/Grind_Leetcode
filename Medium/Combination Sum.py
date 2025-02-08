
class Solution(object):
    def isBalanced(self, num):
        '''

        :param candidates:
        :param target:
        :return:
        '''

        nums = [int(digit) for digit in num]
        sum_odd = 0
        sum_even = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                # odd.append(num)
                sum_even += num
            elif i % 2 == 1:
                # even.append(num)
                sum_odd += num

        if sum_even == sum_odd:
            return True
        else:
            return False

solution = Solution()
print(solution.isBalanced("24123"))


