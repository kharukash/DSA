# Using String
# Time Complexity : O(d)   since d(digits) are converted to string, len is O(1)
# Space Complexity : O(d)  Since extra string with d characters is created

class Solution:
    def countDigit(self, n):
        return len(str(n)) 
    


# Without converting to string
# // is integer division (also called floor division).
# 125 -> 12 -> 1 -> 0      digitscount = 3 
# Time Complexity : O(d)   since loop runs d(digits) times
# Space Complexity : O(1)
#Instance Method 
# self(instance method) is req for accesing object since python secretly converts obj.countDigits(1234) to  Solution.countDigits(obj, 123)  & it has 2 parameters now.

class Solution:
    def countDigits(self,n):
        n = abs(n)
        count = 0
        if n == 0:
            return 1
        while n>0:
            n = n//10
            count +=1
        return count 
  
  
    
obj = Solution()
print(obj.countDigits(1234))