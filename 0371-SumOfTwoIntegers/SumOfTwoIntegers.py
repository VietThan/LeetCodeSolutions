class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        
        # find if abs(a) >= abs(b)
        if x < y: return self.getSum(b, a)
        
        # should be abs(a) >= abs(b)
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            # sum of two positive integers x + y
            # while y/carry is not 0
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        
        else:
            # difference of two integers x - y
            # while y/borrow is not 0
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow
                
        return x * sign
            