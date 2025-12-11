# Using String
# Time Complexity : O(d)   since d(digits) are converted to string, len is O(1)
# Space Complexity : O(d)  Since extra string with d characters is created

class Solution:
    def countDigit(self, n):
        return len(str(n)) 