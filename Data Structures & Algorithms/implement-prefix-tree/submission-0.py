class PrefixTree:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        for char in word:
            if char not in self.children:
                self.children[char] = PrefixTree()
            self = self.children[char]
        
        self.is_end = True

    def search(self, word: str) -> bool:
        for char in word:
            if char not in self.children:
                return False
            self = self.children[char]
        
        return self.is_end

    def startsWith(self, prefix: str) -> bool:
        for char in prefix:
            if char not in self.children:
                return False
            self = self.children[char]
        
        return True
        