class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zeros = 0
        ans = 0

        for R , X in enumerate(nums):
            zeros+=(X==0)

            if zeros > 1:
                zeros-=(nums[l]==0)
                l+=1
            ans = max(ans , R-l)
        return ans