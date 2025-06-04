class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {}
        for i,val in enumerate(nums):
            diff = target - val
            if diff in nums_dict:
                return [nums_dict[diff], i]
            nums_dict[val] = i