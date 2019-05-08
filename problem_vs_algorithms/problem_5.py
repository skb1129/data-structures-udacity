class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.isWordEnd = False

    def __repr__(self):
        return str(list(self.children.keys()))

    def insert(self, char):
        ## Add a child node in this Trie
        if not self.children.get(char):
            self.children[char] = TrieNode()
        return self.children.get(char)

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        result = []
        if self.isWordEnd:
            result.append(suffix)
        for char in self.children:
            result = result + self.children.get(char).suffixes(suffix + char)
        return result

class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        head = self.root
        for char in word:
            head = head.insert(char)
        head.isWordEnd = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        head = self.root
        for char in prefix:
            head = head.children.get(char)
            if not head: return head
        return head


# Testing:
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Interactive
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');
# Interactive
