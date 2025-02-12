class Solution(object):
    def romanToInteger(self, s):

        '''
        Start with s = "MCMXCIV".
            Iterate through the string:
            M = 1000 → Add → result = 1000.
            C = 100, next is M = 1000 → Subtract → result = 1000 - 100 = 900.
            M = 1000 → Add → result = 900 + 1000 = 1900.
            X = 10, next is C = 100 → Subtract → result = 1900 - 10 = 1890.
            C = 100 → Add → result = 1890 + 100 = 1990.
            I = 1, next is V = 5 → Subtract → result = 1990 - 1 = 1989.
            V = 5 → Add → result = 1989 + 5 = 1994.
            Final result: 1994.

        '''

        roman_key = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roman_key[s[i]] < roman_key[s[i+1]]:
                result = result - roman_key[s[i]]
            else:
                result = result + roman_key[s[i]]

        return result
solution = Solution()
strs = "M"
print(solution.romanToInteger(strs))