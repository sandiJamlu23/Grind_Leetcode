class Solution(object):
    def intToRoman(self, num):

        '''
        #Use mapping Instead

        Start with num = 1994.
        Iterate through the roman_map:
            1000 fits into 1994 → Add "M" to the result, subtract 1000 → num = 994.
            900 fits into 994 → Add "CM" to the result, subtract 900 → num = 94.
            90 fits into 94 → Add "XC" to the result, subtract 90 → num = 4.
            4 fits into 4 → Add "IV" to the result, subtract 4 → num = 0.
        Final result: "MCMXCIV".
        '''

        mapping = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        int_to_roman = ""

        for key, value in mapping.items():
            while num >= key:
                int_to_roman = int_to_roman + value
                num = num - key

        return int_to_roman

solution = Solution()
nums = 3749
print(solution.intToRoman(nums))

