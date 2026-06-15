class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumofSquares(n)

        while slow !=  fast:
            fast = self.sumofSquares(fast)
            fast = self.sumofSquares(fast)
            slow = self.sumofSquares(slow)
        return True if fast == 1 else False


    def sumofSquares(self, n: init) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit 
            n = n // 10
        return output