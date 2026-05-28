class Solution:
    delim = '\u001F'
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        encoded_string = self.delim.join(s for s in strs)
        return encoded_string+self.delim
    def decode(self, s: str) -> List[str]:
        decoded = []
        j = 0
        if s == "":
            return decoded
        for i in range(len(s)):
            if s[i] == self.delim:
                decoded.append(s[j:i])
                j = i+1
        return decoded            