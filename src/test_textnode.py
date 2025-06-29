import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode(" is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_notequrl(self):
        node = TextNode("This is a text node", TextType.TEXT, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("A website about World of Warcraft", TextType.LINK, "https://www.mmo-champion.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "A website about World of Warcraft")
        self.assertEqual(html_node.props, {"href": "https://www.mmo-champion.com"})

    def test_image(self):
        node = TextNode("A link to a photo of a bird", TextType.IMAGE, "bird.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "bird.jpg", "alt": "A link to a photo of a bird"})

if __name__ == "__main__":
    unittest.main()