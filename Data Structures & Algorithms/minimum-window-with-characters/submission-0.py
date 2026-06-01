class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m_t = {}
        for c in t:
            m_t[c] = m_t.get(c,0) + 1
        min_sub = [float('inf'), ""]
        for i in range(len(s)):
            if s[i] in m_t:
                m = m_t.copy()
                rem = len(m.keys())
                for j in range(i,len(s)):
                    if s[j] in m:
                        m[s[j]] -= 1
                        if m[s[j]] == 0:
                            rem -= 1
                            if rem == 0:
                                if (j - i + 1) < min_sub[0]:
                                    min_sub[0] = j - i + 1
                                    min_sub[1] = s[i:j+1]
        
        return min_sub[1]