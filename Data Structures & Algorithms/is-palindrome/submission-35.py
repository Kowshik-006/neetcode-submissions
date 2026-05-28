class Solution:
    def isAlphanum(self, c:str)->bool:
        if  ord(c) >= ord('a') and ord(c) <= ord('z'):
            return True
        
        if  ord(c) >= ord('A') and ord(c) <= ord('Z'):
            return True

        if  ord(c) >= ord('0') and ord(c) <= ord('9'):
            return True

        return False
        
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and not self.isAlphanum(s[left]):
                left += 1
            
            while left < right and not self.isAlphanum(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                print(f"Left: {s[left]}")
                print(f"Right: {s[right]}")
                return False
            
            left += 1
            right -= 1
            
        return True