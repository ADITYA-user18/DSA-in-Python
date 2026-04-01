class Solution(object):
    def maximumWealth(self, accounts):

        n = len(accounts)
        store = 0


        for i in range(n):
            summ = sum(accounts[i])
            store = max(store,summ)


        return store



        
