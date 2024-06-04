class Solution(object):
    def maxProfit(self, prices):
        mn=prices[0]
        c=0
        for i in range (1,len(prices)):
            if prices[i]<mn:
                mn=prices[i]
                c=i
        sell =prices[c+1:]
        if len(sell)==0:
            return 0
        else:
            maxp=0
            for s in sell:
                p=s-mn
                if p>maxp:
                    maxp=p
            return maxp


        
        
