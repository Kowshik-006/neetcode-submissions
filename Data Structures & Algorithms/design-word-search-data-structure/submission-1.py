class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        dotcount = 0

        def subSearch(root:TrieNode ,word:str) -> bool:
            nonlocal dotcount
            curr = root

            for i in range(len(word)):
                if word[i] == ".":
                    if dotcount < 2 or True:
                        dotcount += 1
                        for child in curr.children.values():
                            if i == len(word) - 1:
                                return child.endOfWord
                            if subSearch(child, word[i+1:]):
                                return True
                        return False
                    else:
                        return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.endOfWord
        
        return subSearch(self.root, word)
                
                
