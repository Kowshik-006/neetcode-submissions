class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = '\x1F' # Not printable - won't appear in texts
        encoded_string = ''
        for s in strs:
            encoded_string += str(len(s)) + delimiter + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        delimiter = '\x1F'
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != delimiter:
                j += 1
            
            length = int(s[i:j])

            result.append(s[j+1:j+1+length])
            i = j+1+length
        
        return result