# Usine String Slicing
Time : O(d)
Space: O(d)
class Solution:
    def reverseNumber(self, n):
        print(int(str(n)[::-1]))
 
# Usine List reverse()  
Time : O(d)
Space: O(d)     
class Solution:
    def reverseNumber(self, n):
        y = list(str(n))
        y.reverse()
        return int("".join(y))
 
# Without list and String   
Time : O(d)  # loop runs d(digits) times
Space: O(1)  
class Solution:
    def reverseNumber(self, n):
        rev = 0
        neg = n < 0   # True if say -123 so that later if neg it gives -321
        n = abs(n)    # if -123 gives 123
        while n > 0:
            rev = rev * 10 + (n % 10)
            n //= 10

        return -rev if neg else rev
    

            
