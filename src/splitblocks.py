import re

from enum import Enum
from examples import *

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

def block_to_block_type(block):
    lines = block.split("\n")
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
    lst = []
    for b in blocks:
        lst.append(block_to_block_type(b))
    return lst

example = markdown_to_html_node(example_code_md)

print(example)


