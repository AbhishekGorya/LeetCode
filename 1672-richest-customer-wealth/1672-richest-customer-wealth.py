class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxi = 0 
        for i in range(len(accounts)):
            res = sum(accounts[i])
            maxi = max(maxi , res)

        return maxi
        