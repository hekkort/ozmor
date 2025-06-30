import re

from enum import Enum
import examples

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
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
        
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    if all(line.startswith(f"{i + 1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    if lines[0].startswith("```") and lines[len(lines) - 1].endswith("```"):
        return BlockType.CODE
    if re.match(r"^#{1,6} [^\n]+$", lines[0]):
        return BlockType.HEADING
    return BlockType.PARAGRAPH



    # def block_to_block_type(block):
    #     block = markdown_to_blocks(block)
    #     for b in block:
    #         lines = b.split("\n")
    #         if all(line.startswith(">") for line in lines):
    #             return BlockType.QUOTE
    #         if all(line.startswith("- ") for line in lines):
    #             return BlockType.UNORDERED_LIST
    #         if all(line.startswith(f"{lines.index(line) + 1}. ") for line in lines):
    #             return BlockType.ORDERED_LIST
    #         if lines[0].startswith("```") and lines[len(lines) - 1].endswith("```"):
    #             return BlockType.CODE
    #         if re.match(r"^#{1,6} [^\n]+$", lines[0]):
    #             return BlockType.HEADING
    #     return BlockType.PARAGRAPH

for c in examples.code_tests:
    print(block_to_block_type(c))

for o in examples.ordered_tests:
    print(block_to_block_type(o))