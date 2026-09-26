class Solution:
    delim = '\u001f'
    def encode(self, strs: List[str]) -> str:
        # differentiate [] from [""]
        if len(strs) == 0:
            return '\u001e'
        # when [""] returns "", no delim appended
        return self.delim.join(s for s in strs)

    def decode(self, s: str) -> List[str]:
        if s == '\u001e':
            return []
        if s == "":
            return [""]
        
        return s.split(self.delim)
        
        