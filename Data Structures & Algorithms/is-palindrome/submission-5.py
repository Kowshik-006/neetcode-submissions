class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_alphanum_s = ""
        
        for c in s:
            if (ord(c)>=ord('A') and ord(c)<=ord('Z')) or (ord(c)>=ord('a') and ord(c)<=ord('z')) or (ord(c)>=ord('0') and ord(c)<=ord('9')):
                only_alphanum_s +=  c.lower()
        
        rev = only_alphanum_s[::-1]

        if only_alphanum_s == rev:
            return True
        return False
