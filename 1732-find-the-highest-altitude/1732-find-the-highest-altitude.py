class Solution:
    def largestAltitude(self, gain):
        mx = 0
        curr = 0

        for i in gain:
            curr+=i
            mx = max(mx, curr)

        return mx