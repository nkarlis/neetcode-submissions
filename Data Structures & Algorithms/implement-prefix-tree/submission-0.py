class PrefixTreeNode:
    def __init__(self):
        self.children = [None] * 26 # 26 letters of the alphabet
        self.end = False



class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a") # map char to number
            # if the char is not in our trie add it
            if curr.children[i] == None:
                curr.children[i] = PrefixTreeNode()
            # move to the next char
            curr = curr.children[i]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a") # map char to number
            # if the char is not in our trie return False
            if curr.children[i] == None:
                return False
            # move to the next char
            curr = curr.children[i]
        # return true only if its the end of the word in the tree
        return curr.end

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a") # map char to number
            # if the char is not in our trie return False
            if curr.children[i] == None:
                return False
            # move to the next char
            curr = curr.children[i]
        # return true because all the characters of the word are in the trie
        return True

        
        