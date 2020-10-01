class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()

#     def suffixes(self, suffix = ''):
#         ## Recursive function that collects the suffix for 
#         ## all complete words below this point
#         suffixes = []
#         if self.is_word:
#             suffixes.append('')
            
#         if len(self.children) == 0:
#             return suffixes
        
#         for char in self.children:
#             sub_suffixes = [char + i for i in self.children[char].suffixes()]
#             suffixes += sub_suffixes
        
#         return suffixes
    
    def suffixes(self, suffix=''):
        """ Recursive function that collects the suffix for all complete words below this point """

        suffixes = []

        if self.is_word and suffix != '':
            suffixes.append(suffix)

        if len(self.children) == 0:
            return suffixes

        for char in self.children:
            suffixes.extend(self.children[char].suffixes(suffix=suffix+char))

        return suffixes
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            ## if the char not in the node's children
            ## then the prefix does not exist in the Trie
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node
    
    def if_exists(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# Test cases
# test 1
pre_node = MyTrie.find('ant')
print(pre_node.suffixes())
# results: ['hology', 'agonist', 'onym']

# test 2
pre_node = MyTrie.find('f')
print(pre_node.suffixes())
# results: ['un', 'unction', 'actory']

# test 3
pre_node = MyTrie.find('tri')
print(pre_node.suffixes())
# results: ['e', 'gger', 'gonometry', 'pod']

# test 4 - edge case (no suffixes founded)
pre_node = MyTrie.find('antonym')
print(pre_node.suffixes())
# results: []

# test 5 - prefix not in the Trie
pre_node = MyTrie.find('k')
print(pre_node)
# results: pre_node is False and report error when running suffixes function
