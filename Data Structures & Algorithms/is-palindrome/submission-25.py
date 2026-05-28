class Solution:
    def isAlphanum(self, c:str) -> bool:
        return ((ord(c) >= ord('A') and ord(c) <= ord('Z')) or
                (ord(c) >= ord('a') and ord(c) <= ord('z')) or
                (ord(c) >= ord('0') and ord(c) <= ord('9')))
    
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and not self.isAlphanum(s[left]):
                left += 1
            while left < right and not self.isAlphanum(s[right]):
                right -= 1
            
            if left == right: 
                break

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True