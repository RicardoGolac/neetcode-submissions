class TrieNode:
    def __init__(self):
        self.children = {}
        self.IsEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # Adds word to the data structure.
    def addWord(self, word: str) -> None:
        # Initialize the curr pointer with the root node
        current = self.root

        # Iterate across the length of the string
        for c in word:
            # Check if the node exists for the
            # current character in the Trie
            if c not in current.children:
                # If node for current character does
                # not exist then make a new node
                current.children[c] = TrieNode()
            # Move the current pointer to the
            # newly created node
            current = current.children[c]

        # Mark the end of the word
        current.IsEndOfWord = True

    # Returns true if there is any string in the data structure that matches
    # Returns false otherwise
    # Word may contain dots '.' where dots can be matched to any letter
    def search(self, word: str) -> bool:

        def dfs(j, root):
            current = root
            # Iterate through each char in the word
            for i in range(j, len(word)):
                c = word[i]
                # If c is a dot:
                # Check all possible indexes for the remaining word values.
                # BackTrack.
                if c == ".":
                    for child in current.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    # If c is a normal char, check if it exists
                    # If it doesn't exist, the word doesn't exist. Return False
                    if c not in current.children:
                        return False
                    # If it does exist, set the current node to the child node. 
                    # Continue iterating
                    current = current.children[c]
            return current.IsEndOfWord
        
        return dfs(0, self.root)
