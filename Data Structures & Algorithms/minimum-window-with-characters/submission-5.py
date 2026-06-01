class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m_t = {}
        
        for c in t:
            m_t[c] = m_t.get(c,0) + 1
        
        min_sub = [float('inf'), ""]
        have = 0
        need = len(t)
        l = 0
        
        m_s = {}
        
        for r in range(len(s)):
            if s[r] in m_t:
                m_s[s[r]] = m_s.get(s[r],0) + 1
                if m_s.get(s[r],0) <= m_t[s[r]]:
                    have += 1

                    while have == need:
                        if (r-l+1) < min_sub[0]:
                            min_sub[0] = r-l+1
                            min_sub[1] = s[l:r+1]
                        
                        if s[l] in m_s:
                            if m_s[s[l]] <= m_t[s[l]]:
                                have -= 1
                            m_s[s[l]] -= 1

                        
                        l += 1
        return min_sub[1]