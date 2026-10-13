class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in nums[i+1:]:
                nums[i] = None
                return [i, nums.index(goal)] 
        return False
        