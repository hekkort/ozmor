import unittest

from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):
    def test_code(self):
        nodes = [
            TextNode("This is text with a `code block` word", TextType.TEXT),
            TextNode("This is text with a `code block` word", TextType.TEXT),
            TextNode("This is text with a `code block` word", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT, None),
                                    TextNode("code block", TextType.CODE, None),
                                    TextNode(" word", TextType.TEXT, None),
                                    TextNode("This is text with a ", TextType.TEXT, None),
                                    TextNode("code block", TextType.CODE, None),
                                    TextNode(" word", TextType.TEXT, None),
                                    TextNode("This is text with a ", TextType.TEXT, None),
                                    TextNode("code block", TextType.CODE, None),
                                    TextNode(" word", TextType.TEXT, None)])
        
    def test_bold(self):
        nodes = [TextNode("This is text with a **bold word** block and another **bold** word", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT, None),
                                    TextNode("bold word", TextType.BOLD, None),
                                    TextNode(" block and another ", TextType.TEXT, None),
                                    TextNode("bold", TextType.BOLD, None),
                                    TextNode(" word", TextType.TEXT, None)])
    def test_italic(self):
        nodes = [TextNode("This is text with a _bold word_ block and another _bold_ word", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT, None),
                                    TextNode("bold word", TextType.ITALIC, None),
                                    TextNode(" block and another ", TextType.TEXT, None),
                                    TextNode("bold", TextType.ITALIC, None),
                                    TextNode(" word", TextType.TEXT, None)])
    
    def test_exception(self):
        nodes = [TextNode("this is some _text without closing the italic", TextType.TEXT)]
        with self.assertRaises(Exception):
            split_nodes_delimiter(nodes, "_", TextType.ITALIC)
