from textnode import TextNode, TextType

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