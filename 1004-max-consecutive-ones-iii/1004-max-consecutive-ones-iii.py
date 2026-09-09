class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        max_len = 0
        zero_cnt = 0

        while left <= right and right < len(nums):
            if nums[right] == 1:
                max_len = max(max_len, right - left + 1)
                #right += 1

            else:
                zero_cnt += 1
                if zero_cnt > k:
                    # move until left zero is gone
                    if nums[left] == 0: # if left is 0, move only once
                        left += 1
                    else:
                        while(nums[left] != 0): # move left until left is zero
                            left += 1

                        left += 1 # abandon single zero

                else:
                    max_len = max(max_len, right - left + 1)
                    
            right += 1


        return max_len 