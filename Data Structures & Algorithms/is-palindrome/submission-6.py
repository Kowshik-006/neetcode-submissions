class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cln = ""
        
        for c in s:
            if (ord(c)>=ord('A') and ord(c)<=ord('Z')) or (ord(c)>=ord('a') and ord(c)<=ord('z')) or (ord(c)>=ord('0') and ord(c)<=ord('9')):
                s_cln +=  c.lower()
        
        rev = s_cln[::-1]

        if s_cln == rev:
            return True
        return False
