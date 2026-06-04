class Solution:
    def maxProfit(self, price: List[int]) -> int:
        l,r = 0,1
        maxp = 0

        while r<len(price):
            if price[l]<price[r]:
                profit = price[r]-price[l]
                maxp = max(maxp,profit)
            else:
                l=r
            r+=1
        return maxp            