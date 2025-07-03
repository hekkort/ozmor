import re

from enum import Enum
from examples import *
from htmlnode import ParentNode, LeafNode
from textnode import *
from splitnodes import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(md):
    lst = []
    final = []
    blocks = md.split("\n\n")
    for b in blocks:
        lst.append(b.strip())
    for l in lst:
        if l != "":
            final.append(l)
    return final

def block_to_block_type(text):
    lines = text.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    numbered_lines = [line for line in lines if re.match(r'^\d+\. ', line)]
    if numbered_lines:
        numbers = []
        for line in numbered_lines:
            match = re.match(r'^(\d+)\. ', line)
            if match:
                numbers.append(int(match.group(1)))
        expected_sequence = list(range(1, len(numbers) + 1))
        if numbers == expected_sequence:
            return BlockType.ORDERED_LIST
    if lines[0].startswith("```") and lines[len(lines) - 1].endswith("```"):
        return BlockType.CODE
    if re.match(r"^#{1,6} [^\n]+$", lines[0]):
        return BlockType.HEADING
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    parent = ParentNode("div", children)
    for text in blocks:
        children.append(make_node(text))
    return parent

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children = []
    for t in textnodes:
        children.append(text_node_to_html_node(t))
    return children


def make_node(text):
    type = block_to_block_type(text)
    if type == BlockType.HEADING:
        heading_amount = len(re.match(r"^(#+)", text).group(1))
        return ParentNode(f"h{heading_amount}", text_to_children(determine_header_value(text)))
    if type == BlockType.QUOTE:
        return ParentNode("blockquote", text_to_children(determine_quote_value(text)))
    if type == BlockType.UNORDERED_LIST:
        return ParentNode("ul", make_unordered_list_children(text))
    if type == BlockType.ORDERED_LIST:
        return ParentNode("ol", make_ordered_list_children(text))
    if type == BlockType.PARAGRAPH:
        return ParentNode("p", text_to_children(text.replace("\n", " ")))
    if type == BlockType.CODE:
        lines = text.split('\n')
        code_content = '\n'.join(lines[1:-1]) + "\n"
        return ParentNode("pre", [LeafNode("code", code_content)])
    
def determine_header_value(text):
    return re.sub(r"^#{1,6}\s*", "", text)

def determine_quote_value(text):
    lines = text.split("\n")
    final = ""
    for line in lines:
        final += re.sub(r"^(>)", "", line).strip() + " "
    final = final.strip()
    return final

def make_unordered_list_children(text):
    lines = text.split("\n")
    final = []
    for line in lines:
        final.append(ParentNode("li", text_to_children(line.replace("- ", "").strip())))
    return final

def make_ordered_list_children(text):
    lines = text.split("\n")
    final = []
    for line in lines:
        final.append(ParentNode("li", text_to_children(re.sub(r"^\d+\. ", "", line).strip())))
    return final