class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented()
    
    def props_to_html(self):
        string = ""
        for k, v in self.props.items():
            string += f" {k}={v}"
        return string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode should have a value")
        if self.tag == None:
            return self.value
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Must have a tag")
        if self.children == None:
            raise ValueError("Child HTMLNodes are missing")
        final = ""
        string = ""
        
        if self.props:
            for c in self.children:
                string += c.to_html()
            final += f"<{self.tag}{self.props_to_html()}>{string}</{self.tag}>"
            return final

        for c in self.children:
            string += c.to_html()
        final += f"<{self.tag}>{string}</{self.tag}>"
        return final

        