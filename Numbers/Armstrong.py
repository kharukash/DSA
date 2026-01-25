# Space and Time = O(n)
# 153 => 1*^3 + 5^3 + 3*3 = 153 (Armstrong Number)
class Solution:
    def arm(self, n):
        n = abs(n)
        sum = 0
        power = len(str(n))
        for i in str(n):
            sum += int(i) ** power
    
        if sum == n:
            return f"{n} is an Arnstrong number"
        else:
            return f"{n} is not an Arnstrong number"
    
obj = Solution()
print(obj.arm(153))
