class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i , nums in enumerate(nums):
            compliment = target - nums

            if compliment in seen:
                return [seen[compliment] , i]

            seen[nums] = i
        