class Solution(object):
    def permutate(self, nums):

        '''
        Initial call: permute([1,2,3])

            Pop 1, recursively call permute([2,3])
            Store 1 for later


            permute([2,3])

            Pop 2, recursively call permute([3])
            Store 2 for later


            permute([3])

            Base case: return [[3]]


            Back to permute([2,3])

            Add 2 to [3]: [3,2]
            Put 2 back, pop 3
            Get permutations with 3 first: [2,3]
            Result: [[3,2], [2,3]]


            Finally, permute([1,2,3])

            Add 1 to each permutation from step 4
            Continue with 2 and 3 as first elements

            graph TD
            A([1,2,3]) --> B([2,3])
            A --> C([1,3])
            A --> D([1,2])

            B --> E([3])
            B --> F([2])

            C --> G([3])
            C --> H([1])

            D --> I([2])
            D --> J([1])

            E --> K[[3,2,1]]
            F --> L[[2,3,1]]

            G --> M[[1,3,2]]
            H --> N[[3,1,2]]

            I --> O[[1,2,3]]
            J --> P[[2,1,3]]

        '''

        # base Case: if only one number, return it as a list of list
        if len(nums) == 1:
            return [nums[:]] # return whichever that number in nums

        # store the permutate in result
        result = []

        # for each number in nums
        for i in range (len(nums)):
            # remove current number
            n = nums.pop(0)

            # get permutations of remaining numbers
            perms = self.permutate(nums)

            # add current number to each permutations
            for perm in perms:
                perm.append(n)
            result.extend(perms)

            # put the number back for next iterations
            nums.append(n)
        return result

solution = Solution()
print(solution.permutate([1,2,3]))