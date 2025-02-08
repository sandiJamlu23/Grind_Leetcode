class Solution(object):
    def numberGame(self, nums):
        '''
        6,4,7,8

        del 4 -> 6, 7, 8. arr = 4
        del 6 -> 7, 8     arr = 6,4

        del 7 -> 8        arr = 7,6,4
        del 8 ->          arr = 8,7,6,4
        '''
        # find min in current list
        '''arr = []
                i = 0
                nums.sort()
        
                while i < len(nums):
        
                    # take the first min value
                    first_element = nums[i]
                    second_element = nums[i+1]
        
                    arr.append(second_element)
                    arr.append(first_element)
        
                    i += 2
        
                return arr '''

        arr = []

        while nums:
            alice_min = min(nums)
            nums.remove(alice_min)
            if nums:
                bob_min = min(nums)
                nums.remove(bob_min)

                arr.append(bob_min)
            arr.append(alice_min)

        return arr
solution = Solution()
print(solution.numberGame([1,4,2,5]))