class Solution(object):
    def reverseVowels(self, s):


        su = list(s)
        vowels = {'a','e','i','o','u','A','E','I','O','U'}

        left = 0
        right = len(su)-1

        while left<right:
            if su[left] in vowels and su[right] in vowels:
                su[left],su[right]=su[right],su[left]
                left+=1
                right-=1

            elif su[left] in vowels and su[right] not in vowels:
                right-=1

            elif su[right] in vowels and su[left] not in vowels:
                left+=1

            else:
                left+=1
                right-=1



        return "".join(su)
        
        
