import unittest

from main import *

class TestMain(unittest.TestCase):

    def test_extract_markdown(self):

        test = extract_title(lorithal)
        test2 = "🌍 The **Curious World of Lorithal**"

        self.assertEqual(test, test2)
