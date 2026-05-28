class Solution:
    def isAlphanum (self,s:str) -> bool:
        return ((ord('a') <= ord(s) and ord(s) <= ord('z')) or 
                (ord('A') <= ord(s) and ord(s) <= ord('Z')) or 
                (ord('0') <= ord(s) and ord(s) <= ord('9')))

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            while not self.isAlphanum(s[left]) and left < right:
                left += 1
            while not self.isAlphanum(s[right]) and left < right:
                right -=1

            if left == right:
                break
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True