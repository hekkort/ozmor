import unittest

from textnode import TextNode, TextType
from examples import *
from splitblocks import *

class TestSplitBlocks(unittest.TestCase):

    def test_blocks_to_block_type(self):
        pass



    def test_markdown_to_blocks(self):
        md = """




This is **bolded** paragraph





This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line





- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )