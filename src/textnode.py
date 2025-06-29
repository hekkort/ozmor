from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
    TEXT = None
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        if self.text == value.text:
            if self.text_type == value.text_type:
                if self.url == self.url:
                    return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Invalid TextType")
    if text_node.text_type.value == "a":
        return LeafNode(text_node.text_type.value, text_node.text, {"href": text_node.url})
    if text_node.text_type.value == "img":
        return LeafNode(text_node.text_type.value, "", {"src": text_node.url, "alt": text_node.text})
    else:
        return LeafNode(text_node.text_type.value, text_node.text)