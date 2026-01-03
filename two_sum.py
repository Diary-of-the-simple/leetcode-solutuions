class Solution:

	def twoSum(self, nums: List[int], target: int) -> List[int]:
		pairs = {}
		
		for i, val in enumerate(nums):
			complement = target - val
			if complement in pairs:
				return[pairs[complement], i]
			pairs[val] = i
