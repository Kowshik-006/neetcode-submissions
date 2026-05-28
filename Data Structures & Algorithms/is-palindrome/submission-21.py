class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cln = ""
        
        for c in s:
            if (ord(c)>=ord('A') and ord(c)<=ord('Z')) or (ord(c)>=ord('a') and ord(c)<=ord('z')) or (ord(c)>=ord('0') and ord(c)<=ord('9')):
                s_cln +=  c.lower()

        for i in range(len(s_cln)//2):
            if s_cln[i] != s_cln[len(s_cln)-1-i]:
                return False

        return True
