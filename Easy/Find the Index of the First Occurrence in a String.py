
class Solution(object):
    def findOccurance(self, haystack, needle):
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

solution = Solution()
print(solution.findOccurance("sadbutsad", "sad"))
