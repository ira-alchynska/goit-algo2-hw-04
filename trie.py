class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        """Initialize an empty trie."""
        self.root = TrieNode()

    def put(self, key: str, value=None):
        """
        Insert a word into the trie. Value is ignored in this simple implementation,
        but kept for compatibility.
        """
        node = self.root
        for ch in key:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def _collect(self, node: TrieNode, prefix: str, results: list):
        """
        Recursively collect all words under this node.
        """
        if node.is_end:
            results.append(prefix)
        for ch, child in node.children.items():
            self._collect(child, prefix + ch, results)

    def keys(self) -> list:
        """
        Return all words stored in the trie.
        """
        results = []
        self._collect(self.root, "", results)
        return results

    def _get_node(self, prefix: str):
        """
        Traverse the trie to the node representing the end of prefix.
        Return None if prefix is not in the trie.
        """
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def keys_with_prefix(self, prefix: str) -> list:
        """
        Return all stored words that start with the given prefix.
        """
        node = self._get_node(prefix)
        if node is None:
            return []
        results = []
        self._collect(node, prefix, results)
        return results
