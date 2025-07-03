class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x = str(x)
            reverse_x = x[::-1]
            if (x != reverse_x):
                return False
            else:
                return True