'''

nums1 = [1,2,3,0,0,0], m=3
nums2 = [2,4,5], n=3

nums1[0] = 1 vs nums2[0] = 2
nums1[i] vs nums2[j]

goal = [1,2,2,3,4,5], with the n = 6, which is just m+n
    * compare each element, make if statement to find which is smaller and store the result in the-
    new list.
    * the largest of the current comparison is placed next to the smallest.

'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1, p2, p = m-1, n-1, m+n-1

        while p1 >= 0 and p2 >= 0: # until it reach the 0 element
            if nums1[p1] > nums2[p2]:
                # let's say we have a new arr to store the result
                ''' 
                but, instead of place it in the new array, return the nums1-
                that has been merged with nums2
                '''
                # merge_arr.append(nums1[i])
                nums1[p] = nums1[p1]
                p1 -= 1 # work backwards
            else:
                # merge_arr.append(nums2[j])
                # j = j + 1
                nums1[p] = nums2[p2]
                p2 -= 1

            p -= 1 # fill the padding

        # add the remaining
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

solution = Solution()
nums1 = [2,0] # the zero elements are called padding.
nums2 = [1]

solution.merge(nums1, 1, nums2, 1)  # Merge nums2 into nums1
print(nums1)

