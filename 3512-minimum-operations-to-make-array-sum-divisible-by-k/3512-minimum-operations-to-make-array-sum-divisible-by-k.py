class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = sum(nums)
        rem = 0
        
        # Keep looping until res is perfectly divisible by k
        while res % k != 0:
            rem += 1
            res -= 1
            
        return rem