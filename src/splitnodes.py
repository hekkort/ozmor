import re

from textnode import TextNode, TextType
from examples import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for o in old_nodes:
        if o.text_type != TextType.TEXT:
            new_nodes.append(o)
        else:
            splitted = o.text.split(delimiter)
            if len(splitted) % 2 == 0:
                raise Exception("Closing delimiter not found")
            for i in range(len(splitted)):
                if i % 2 != 0:
                    new_nodes.append(TextNode(splitted[i], text_type))
                else:
                    new_nodes.append(TextNode(splitted[i], TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
    
def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_link(old_nodes):

    result = []
    new_nodes = []

    for n in old_nodes:
        if n.text_type == TextType.TEXT:
            result = re.split(r'(?=\[)|(?<=\))', n.text)
            if result[len(result) - 1] == "":
                del result[-1]
            for r in result:
                matches = extract_markdown_links(r)
                if not matches:
                    new_nodes.append(TextNode(r, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(matches[0][0], TextType.LINK, matches[0][1]))
        else:
            new_nodes.append(n)

    return new_nodes

def split_nodes_image(old_nodes):

    result = []
    new_nodes = []

    for n in old_nodes:
        if n.text_type == TextType.TEXT:
            result = re.split(r'(?=!)|(?<=\))', n.text)
            if result[len(result) - 1] == "":
                del result[-1]
            for r in result:
                matches = extract_markdown_images(r)
                if not matches:
                    new_nodes.append(TextNode(r, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(matches[0][0], TextType.IMAGE, matches[0][1]))
        else:
            new_nodes.append(n)

    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    for n in nodes:
        if n.text == "":
            nodes.remove(n)
    return nodes
