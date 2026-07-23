class Solution(object):
    def isHappy(self, n):

        seen =  set()
  
        def hi(n,seen):
            if n==1:
                return True 
  
            if n in seen:
                return False

            seen.add(n)  

            string = str(n)
            lister =  list(string)
 
            for i in range(len(lister)):
                lister[i]=int(lister[i])

            total = 0

            for i in range(len(lister)):
                total+=lister[i]**2


            return hi(total,seen)
        return hi(n,seen)


        

        
