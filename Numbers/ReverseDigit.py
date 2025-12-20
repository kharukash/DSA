#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Without list and String   
Time : O(d)  # loop runs d(digits) times
Space: O(1) 

class Solution:
    def reverseNumber(self, n):
        rev = 0
        neg = n < 0   # True if say -123 so that later if neg it gives -321
        n = abs(n)    # if -123 gives 123
        while n > 0:
            rev = rev * 10 + (n % 10)      # % gives remainder
            n //= 10     # // gives quotient
        
        if rev > (2**31 - 1):
            return 0
        return -rev if neg else rev


# Usine List reverse()  
#Time : O(d)
#Space: O(d) 
    
class Solution:
    def reverse(self, n: int) -> int:
       neg = n<0
       n= abs(n)
       y = list(str(n))
       y.reverse()
       rev = int("".join(y))
       if rev > (2**31 - 1):    
           return 0
       return -rev if neg else rev  



#Using String:
#Space and Time : O(d)

class Solution:
    def reverse(self, n: int) -> int:
        neg = n<0
        n = abs(n)
        rev = str(n)[::-1]
        rev = int(rev)
        if rev > (2**31)-1:
            return 0   
