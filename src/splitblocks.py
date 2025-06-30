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
    temp = []
    final = []
    blocks = md.split("\n\n")
    for b in blocks:
        lst.append(b.strip())
    for l in lst:
        if l != "":
            temp.append(l)
    for t in temp:
        final.append(re.sub(r"\s+\n", "\n", t))
    return final

def block_to_block_type(block):
    block = markdown_to_blocks(block)
    for b in block:
        pass