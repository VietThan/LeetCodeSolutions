# Python2

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
	# dict
	# key = number
	# value = index
        differences = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in differences:
                return [differences[diff], i]
            
            differences[nums[i]] = i
