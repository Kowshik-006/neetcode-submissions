class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def insert(self, word: str) -> None:
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endOfWord = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()

        for word in words:
            trie.insert(word)
            
        self.rows, self.cols = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r,c,node,word):
            if (r < 0 or c < 0 or r == self.rows or c == self.cols 
            or board[r][c] not in node.children or (r,c) in visited):
                return 
            
            visited.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                res.add(word)
            
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)

            visited.remove((r,c))
        
        for r in range(self.rows):
            for c in range(self.cols):
                dfs(r,c,trie,"")

        return list(res)
        
