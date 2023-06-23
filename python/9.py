class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        if (x < 100) and (x % 11 == 0):
            return True
        y = 0
        while y < x:
            if y > 0:
                y = y * 10
            y += x % 10
            if x == y:
                return True
            x = int(x / 10)
        if x == y:
            return True
        else:
            return False