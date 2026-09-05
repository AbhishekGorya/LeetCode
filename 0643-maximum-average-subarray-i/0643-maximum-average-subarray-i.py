class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        winmx = sum(nums[:k])
        mx = winmx

        for i in range(k, len(nums)):
            winmx = winmx - nums[i-k] +nums[i]
            mx = max(mx , winmx)

        return mx/k