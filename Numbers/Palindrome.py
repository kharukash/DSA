#Half reverse way   ,Can be done fully also this is little faster though same O(n)
# Time: O(n/2) => O(n)
# Space: O(1)
class Solution:
    def isPalindrome(self, n):
        revhalf = 0
        if n <0 or(n%10==0 and n!=0):
            return False
        while n>revhalf:
            revhalf = (revhalf *10 )+ n%10
            n//=10
        
        if n == revhalf or n == revhalf//10:
            return True
        
        return False
        
        
# Using String Slicing
# Both Time and Space = O(n)
class Solution:
    def isPalindrome(self, n):
        if str(n) == str(n)[::-1]:
            return True  
        else:
            return False
        