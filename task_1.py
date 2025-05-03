import logging
from trie import Trie

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class Homework(Trie):
    def __init__(self):
        super().__init__()
        # Auxiliary trie for reversed words to support efficient suffix queries
        self._rev_trie = Trie()
        logger.debug("Initialized Homework with main trie and reversed trie.")

    def put(self, key, value):
        """
        Insert a word into both the main trie and the reversed trie.
        Raise TypeError if key is not a string.
        """
        if not isinstance(key, str):
            logger.error("Key must be a string. Provided: %s", type(key))
            raise TypeError("Key must be a string")
        super().put(key, value)
        self._rev_trie.put(key[::-1], value)
        logger.debug("Inserted key '%s' with value '%s' into both tries.", key, value)

    def count_words_with_suffix(self, pattern) -> int:
        """
        Count how many stored words end with the given suffix pattern.
        Uses reversed trie to avoid scanning all words.
        Raises TypeError if pattern is not a string.
        """
        if not isinstance(pattern, str):
            logger.error("Pattern must be a string. Provided: %s", type(pattern))
            raise TypeError("Pattern must be a string")
        if pattern == "":
            logger.debug("Empty pattern provided. Returning 0.")
            return 0
        rev_pat = pattern[::-1]
        count = len(self._rev_trie.keys_with_prefix(rev_pat))
        logger.debug("Counted %d words with suffix '%s'.", count, pattern)
        return count

    def has_prefix(self, prefix) -> bool:
        """
        Check if there is at least one stored word starting with prefix.
        Raises TypeError if prefix is not a string.
        """
        if not isinstance(prefix, str):
            logger.error("Prefix must be a string. Provided: %s", type(prefix))
            raise TypeError("Prefix must be a string")
        result = bool(self.keys_with_prefix(prefix))
        logger.debug("Prefix '%s' exists: %s", prefix, result)
        return result

if __name__ == "__main__":
    logger.info("Starting main block.")
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)
        logger.info("Added word '%s' with index %d.", word, i)

    # test count_words_with_suffix
    assert trie.count_words_with_suffix("e") == 1 
    assert trie.count_words_with_suffix("ion") == 1  
    assert trie.count_words_with_suffix("a") == 1    
    assert trie.count_words_with_suffix("at") == 1  
    assert trie.count_words_with_suffix("") == 0    

    # test has_prefix
    assert trie.has_prefix("app") is True   
    assert trie.has_prefix("bat") is False
    assert trie.has_prefix("ban") is True  
    assert trie.has_prefix("ca") is True    

    logger.info("All tests passed.")
    print("All tests passed.")