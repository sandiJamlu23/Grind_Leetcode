class Solution(object):
    def isPalindrome(self, x):
        num = str(x)
        start = 0
        backward = len(num) - 1
        while start < backward:
            if num[start] != num[backward]:
                return False
            start += 1
            backward -= 1

        return True


solution = Solution()
print(solution.isPalindrome(111))
