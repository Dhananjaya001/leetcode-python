class Solution(object):
    def maxProfit(self, prices):
        mn=prices[0]
        mxp=0
        for i in range(1,len(prices)):
            if prices[i]<mn:
                mn=prices[i]
            if mxp<prices[i]-mn:
                mxp=prices[i]-mn

        return mxp
