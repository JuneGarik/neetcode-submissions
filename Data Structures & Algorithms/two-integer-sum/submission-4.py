class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in nums[i+1:]:
                return [i, nums.index(goal, i+1)] 
        return False
        