import logging
from trie import Trie

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        """
        Find the longest common prefix among all strings in the input list.
        Raises TypeError if input is not a list of strings.
        Returns empty string if list is empty or no common prefix.
        Time complexity: O(S), S = total length of all strings.
        """
        # Validate input type
        if not isinstance(strings, list):
            logger.error("Input must be a list of strings. Provided: %s", type(strings))
            raise TypeError("Input must be a list of strings")
        if not strings:
            logger.debug("Empty list provided. Returning empty string.")
            return ""
        for s in strings:
            if not isinstance(s, str):
                logger.error("All elements of input list must be strings. Invalid element: %s", type(s))
                raise TypeError("All elements of input list must be strings")

        logger.debug("Building trie for input strings: %s", strings)
        # Build trie of all input words
        for s in strings:
            self.put(s)
            logger.debug("Inserted string '%s' into trie.", s)

        # Traverse down trie until a branching or end-of-word is encountered
        prefix = ""
        node = self.root
        while True:
            # stop if this node marks end of a word
            if node.is_end:
                logger.debug("End of word reached in trie. Current prefix: '%s'", prefix)
                break
            # stop if more than one child
            if len(node.children) != 1:
                logger.debug("Branching encountered in trie. Current prefix: '%s'", prefix)
                break
            # descend the single child
            ch, next_node = next(iter(node.children.items()))
            prefix += ch
            node = next_node
        logger.debug("Longest common prefix found: '%s'", prefix)
        return prefix

if __name__ == "__main__":
    logger.info("Starting main block.")
    # Tests
    tester1 = LongestCommonWord()
    assert tester1.find_longest_common_word(["flower", "flow", "flight"]) == "fl"
    logger.info("Test 1 passed.")

    tester2 = LongestCommonWord()
    assert tester2.find_longest_common_word([
        "interspecies", "interstellar", "interstate"
    ]) == "inters"
    logger.info("Test 2 passed.")

    tester3 = LongestCommonWord()
    assert tester3.find_longest_common_word(["dog", "racecar", "car"]) == ""
    logger.info("Test 3 passed.")

    # Edge cases
    tester4 = LongestCommonWord()
    assert tester4.find_longest_common_word([]) == ""
    logger.info("Edge case 1 passed: Empty list.")

    try:
        LongestCommonWord().find_longest_common_word("not a list")
    except TypeError:
        logger.info("Edge case 2 passed: Non-list input raised TypeError.")
    else:
        raise AssertionError("TypeError not raised for non-list input")

    try:
        LongestCommonWord().find_longest_common_word(["ok", 123])
    except TypeError:
        logger.info("Edge case 3 passed: Non-string element raised TypeError.")
    else:
        raise AssertionError("TypeError not raised for non-string element")

    logger.info("All tests passed.")
    print("All tests passed.")