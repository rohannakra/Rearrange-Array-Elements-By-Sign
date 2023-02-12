# https://leetcode.com/problems/rearrange-array-elements-by-sign/

def rearrange_array(nums):
    rearranged = []
    
    positive_nums = [num for num in nums if num > 0]
    negative_nums = [num for num in nums if num < 0]
    
    for num1, num2 in zip(positive_nums, negative_nums):
        rearranged.append(num1)
        rearranged.append(num2)
    
    return rearranged

print(rearrange_array([3,1,-2,-5,2,-4]))
print(rearrange_array([-1, 1]))

# ------------------------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        rearranged = []
    
        positive_nums = [num for num in nums if num > 0]
        negative_nums = [num for num in nums if num < 0]
    
        for num1, num2 in zip(positive_nums, negative_nums):
            rearranged.append(num1)
            rearranged.append(num2)
    
        return rearranged
