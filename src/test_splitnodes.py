import unittest

from textnode import TextNode, TextType
from splitnodes import *
from examples import *

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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_negative(self):
        matches = extract_markdown_images(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links_negative(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_no_link(self):
        matches = extract_markdown_images(
            "This is text with an ![image](zjjcJKZ)"
        )
        self.assertListEqual([("image", "zjjcJKZ")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_images(
            "This is text with an ![image](hallodoei)"
        )
        self.assertListEqual([("image", "hallodoei")], matches)
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link to a website](https://i.imgur.com/zjjcJKZ.png) and another [link to a website](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link to a website", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "link to a website", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links_bold(self):
        new_nodes =  split_nodes_link(link_and_bold_nodes)
        self.assertListEqual(
            
            [
                TextNode("Learn **Python** at ", TextType.TEXT, None),
                TextNode("Real Python", TextType.LINK, "https://realpython.com"),
                TextNode(" or visit ", TextType.TEXT, None),
                TextNode("Python.org", TextType.LINK, "https://www.python.org"),
                TextNode(".", TextType.TEXT, None),
                TextNode("Join **communities** like ", TextType.TEXT, None),
                TextNode("Reddit", TextType.LINK, "https://www.reddit.com"),
                TextNode(" or get help on ", TextType.TEXT, None),
                TextNode("Stack Overflow", TextType.LINK, "https://stackoverflow.com"),
                TextNode(".", TextType.TEXT, None)
            ],
            new_nodes
        )
    
    def test_text_to_textnodes(self):
        result = []
        for e in example_text:
            result.append(text_to_textnodes(e))
        for r in result:
            self.assertListEqual([TextNode("This is ", TextType.TEXT, None),
                                TextNode("text", TextType.BOLD, None),
                                TextNode(" with an ", TextType.TEXT, None),
                                TextNode("italic", TextType.ITALIC, None),
                                TextNode(" word and a ", TextType.TEXT, None),
                                TextNode("code block", TextType.CODE, None),
                                TextNode(" and an ", TextType.TEXT, None),
                                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg)"),
                                TextNode(" and a ", TextType.TEXT, None),
                                TextNode("link", TextType.LINK, "https://boot.dev")], r)


    
