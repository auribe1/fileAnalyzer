import unittest

from analyzer import normalizeText, filterWords, countWords

class TestAnalyzer(unittest.TestCase):
    def test_normalizeText_strips_punctuation(self):
        text = "Hello, World!!!"
        self.assertEqual(normalizeText(text), "Hello World")

    def test_filterWords_removes_stopwords(self):
        words = ["the", "robot", "and", "match"]
        stop = {"the", "and"}
        self.assertEqual(filterWords(words=words, stop_words=stop), ["robot", "match"])

    def test_countWords_counts_correctly(self):
        words = ["aaa", "bbb", "aaa"]
        self.assertEqual(countWords(words=words), {"aaa": 2, "bbb" : 1})

if __name__ == "__main__":
    unittest.main()