import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        htmlnode = HTMLNode("p", "wat leuks", children=None, props={"href": "https://www.google.com", "target": "_blank",})
        expected = "HTMLNode(p, wat leuks, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(expected, str(htmlnode))

    def test_props_to_html(self):
        htmlnode = HTMLNode("p", "wat leuks", children=None, props={"href": "https://www.google.com", "target": "_blank",})
        example = htmlnode.props_to_html()
        expected = " href=https://www.google.com target=_blank"
        self.assertEqual(example, expected)

    def test_eq(self):
        node = HTMLNode("p", "wat leuks", children=None, props={"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("p", "wat", children=None, props={"href": "https://www.google.com", "target": "_blank",})
        self.assertNotEqual(node, node2)
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=https://www.google.com>Hello, world!</a>")
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "just some text")
        expected = "<p>just some text</p>"
        self.assertEqual(node.to_html(), expected)
    
    def test_parent_to_html_no_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

        self.assertEqual(node.to_html(), expected)
    
    def test_parent_to_html_props(self):
        node = ParentNode(
            "b",
            [
                LeafNode("a", "Hello, world!", props={"href": "https://www.google.com"}),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )

        expected = "<b><a href=https://www.google.com>Hello, world!</a><b>Bold text</b>Normal text<i>italic text</i>Normal text</b>"

        self.assertEqual(node.to_html(), expected)
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
