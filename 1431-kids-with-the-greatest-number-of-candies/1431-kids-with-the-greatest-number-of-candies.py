class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = []
        curr_max = max(candies)

        for i in candies:
            if i + extraCandies >= curr_max:
                l.append(True)
            else:
                l.append(False)
        return l
