from textnode import TextNode, TextType

lorithal = """# 🌍 The **Curious World of Lorithal**

Welcome to the ancient world of **Lorithal**, a land of forgotten ruins, whispering forests, and floating cities. This document explores its secrets.

---

## 📖 Table of Contents

1. [The History](#the-history)
2. [Creatures of the Realm](#creatures-of-the-realm)
3. [Artifacts & Relics](#artifacts--relics)
4. [Appendix](#appendix)

---

## 🏰 The History

> “Even the stars remember Lorithal, though we have long forgotten her name.” — *Archivist Elen Taar*

Lorithal was once ruled by seven High Houses. The most powerful, **House Veyr**, built the Skyforge — a structure so vast it eclipsed the sun.

### Subsection: The Fall

In the year 8232 of the Third Cycle, the *Gloom Spires* erupted, casting ash across the continent. Survivors tell of a black-winged beast seen circling above the capital.

---

## 🐉 Creatures of the Realm

- **Skirvel Hawks**: Messengers that can travel 300 leagues without rest.
- **Gravetooth Bears**: Their roars shake stone.
- **Glass Serpents**: Almost invisible, they nest in the spires.

---

## 🧭 Artifacts & Relics

1. `Skyforge Compass`  
   Allows the user to find their way even in voidlight.
2. `Shard of Vael`  
   Said to contain a frozen moment in time. *Handle with caution.*
3. `Whispering Ring`  
   - [x] Still functional  
   - [ ] Cursed  
   - [x] Bound to the House of Silence

---

## ⚙️ Code of the Wanderer

```
class Wanderer:
    def __init__(self, name):
        self.name = name
        self.items = []
    def find(self, item):
        self.items.append(item)
        return f"{self.name} found {item}!"
```
"""

code_tests = [
    # ✅ Basic correct case
    """```
1 First line
2 Second line
3 Third line
```""",

    # ✅ Case with leading spaces
    """```
   1 First line
 2 Second line
     3 Third line
```""",

    # ❌ Incorrect sequence
    """```
1 First line
3 Second line
4 Third line
```""",

    # ❌ Starts with 0
    """```
0 Start
1 Continue
2 Continue
```""",

    # ❌ One line missing a number
    """```
1 Good
2 Also good
Oops this line has no number
4 Skipped one
```""",

    # ❌ Non-numeric prefix
    """```
1 First line
two Second line
3 Third line
```""",

    # ✅ Long lines and text after number
    """```
1 This is a very long line that continues with a lot of information
2 Here is another long paragraph of text following the number
3 And it ends here
```""",

    # ❌ Empty line in between
    """```
1 First line

3 Third line
```""",

    # ✅ One line only
    """```
1 Single line only
```""",

    # ❌ No lines
    """```
```"""
]

ordered_tests = [
    # ✅ Basic ordered list
    "1. First item\n2. Second item\n3. Third item",

    # ✅ Leading spaces removed from each line
    "1. First item\n2. Second item\n3. Third item",

    # ❌ Out of order
    "1. First item\n3. Second item\n4. Third item",

    # ❌ Starts at 0
    "0. Start\n1. Continue\n2. Continue",

    # ❌ One item missing a number
    "1. Good\n2. Also good\nOops this item has no number\n4. Skipped one",

    # ❌ Non-numeric prefix
    "1. First item\ntwo. Second item\n3. Third item",

    # ✅ Long lines with list items
    "1. This is a very long item that continues with a lot of description and explanation\n"
    "2. Another long item that provides context and example usage\n"
    "3. A final long item that wraps things up nicely",

    # ❌ Empty line in between
    "1. First item\n\n3. Third item",

    # ✅ One item only
    "1. Single item only",

    # ❌ No content
    ""
]





quote_block = """> This is a blockquote.  
> It can span multiple lines and is often used for citing sources or highlighting ideas."""

md = """


# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

        - This is the first list item in a list block
- This is a list item
- This is another list item          """

wrong_examples = [
    "This is **bold text** with an _italic_ word and a `code snippet` and an ![image](https://example.com/img.png) plus a [valid link](https://example.com).",
    
    "Here is **bold without end and an _italic with *wrong nesting_ and a `code block without close.",
    
    "A broken image markdown ![missing alt text](https://example.com) and a bad link [broken](example) without proper URL.",
    
    "Mixing *italic* and **bold* improperly and some `inline code with no backtick.",
    
    "An exclamation mark before link ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and a [link with missing bracket(https://boot.dev",
    
    "Normal **bold** and _italic_ but this one has a ![bad image](htt://badurl) with wrong URL scheme.",
    
    "Escaped \\*not bold\\* but this one is **bold** and a link without closing parenthesis [link](https://example.com",
]

example_text = ["This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"]

examples = [
    "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
    
    "Try **bold** text combined with _italic_ and `inline code` plus an image ![sunset](https://example.com/sunset.jpg) and a [website](https://example.com).",
    
    "Here's some _italicized text_, some **strong emphasis**, and a `snippet of code`. See this image: ![cat](https://placekitten.com/200/300) and visit [Google](https://google.com).",
    
    "Mix **bold** with _italic_, add a `code block`, an image ![logo](https://logo.clearbit.com/github.com), and a [GitHub link](https://github.com).",
    
    "Using `inline code` inside a sentence with **bold** and _italic_, plus ![mountain photo](https://images.unsplash.com/photo-1506744038136-46273834b3fb) and [Unsplash](https://unsplash.com).",
    
    "Example with multiple links: [First link](https://first.com), [Second link](https://second.com), plus ![icon](https://icons.example.com/icon.png) and some **bold text**.",
]

link_nodes = [
    TextNode(
        "Learn Python at [Real Python](https://realpython.com) or read docs at [Python.org](https://www.python.org).",
        TextType.TEXT,
    ),
    TextNode(
        "Explore [Reddit](https://www.reddit.com) for communities or visit [Stack Overflow](https://stackoverflow.com) for coding help.",
        TextType.TEXT,
    )
]

link_and_bold_nodes = [
    TextNode(
        "Learn **Python** at [Real Python](https://realpython.com) or visit [Python.org](https://www.python.org).",
        TextType.TEXT,
    ),
    TextNode(
        "Join **communities** like [Reddit](https://www.reddit.com) or get help on [Stack Overflow](https://stackoverflow.com).",
        TextType.TEXT,
    )
]


italic_nodes = [
    TextNode(
        "Learn *Python* through tutorials and official documentation.",
        TextType.TEXT,
    ),
    TextNode(
        "*Reddit* and *Stack Overflow* are great places to ask programming questions.",
        TextType.TEXT,
    ),
    TextNode(
        "Reading *tech news* regularly helps you stay updated with the industry.",
        TextType.TEXT,
    ),
    TextNode(
        "Choosing the right *font* and *icon set* can improve your UI design.",
        TextType.TEXT,
    ),
    TextNode(
        "Use *code formatters* and *linters* to keep your codebase clean and consistent.",
        TextType.TEXT,
    ),
    TextNode(
        "Stay up to date with *professional news* and updates from your network.",
        TextType.TEXT,
    ),
    TextNode(
        "Solving *coding challenges* regularly improves problem-solving skills.",
        TextType.TEXT,
    ),
]


code_nodes = [
    TextNode(
        "Learn `Python` through tutorials and official documentation.",
        TextType.TEXT,
    ),
    TextNode(
        "`Reddit` and `Stack Overflow` are great places to ask programming questions.",
        TextType.TEXT,
    ),
    TextNode(
        "Reading `tech news` regularly helps you stay updated with the industry.",
        TextType.TEXT,
    ),
    TextNode(
        "Choosing the right `font` and `icon set` can improve your UI design.",
        TextType.TEXT,
    ),
    TextNode(
        "Use `code formatters` and `linters` to keep your codebase clean and consistent.",
        TextType.TEXT,
    ),
    TextNode(
        "Stay up to date with `professional news` and updates from your network.",
        TextType.TEXT,
    ),
    TextNode(
        "Solving `coding challenges` regularly improves problem-solving skills.",
        TextType.TEXT,
    ),
]


bold_nodes = [
    TextNode(
        "Learn **Python** through tutorials and official documentation.",
        TextType.TEXT,
    ),
    TextNode(
        "**Reddit** and **Stack Overflow** are great places to ask programming questions.",
        TextType.TEXT,
    ),
    TextNode(
        "Reading **tech news** regularly helps you stay updated with the industry.",
        TextType.TEXT,
    ),
    TextNode(
        "Choosing the right **font** and **icon set** can improve your UI design.",
        TextType.TEXT,
    ),
    TextNode(
        "Use **code formatters** and **linters** to keep your codebase clean and consistent.",
        TextType.TEXT,
    ),
    TextNode(
        "Stay up to date with **professional news** and updates from your network.",
        TextType.TEXT,
    ),
    TextNode(
        "Solving **coding challenges** regularly improves problem-solving skills.",
        TextType.TEXT,
    ),
]


text_nodes = [
    TextNode(
        "Learn Python through tutorials and official documentation.",
        TextType.TEXT,
    ),
    TextNode(
        "Reddit and Stack Overflow are great places to ask programming questions.",
        TextType.TEXT,
    ),
    TextNode(
        "Reading tech news regularly helps you stay updated with the industry.",
        TextType.TEXT,
    ),
    TextNode(
        "Choosing the right font and icon set can improve your UI design.",
        TextType.TEXT,
    ),
    TextNode(
        "Use code formatters and linters to keep your codebase clean and consistent.",
        TextType.TEXT,
    ),
    TextNode(
        "Stay up to date with professional news and updates from your network.",
        TextType.TEXT,
    ),
    TextNode(
        "Solving coding challenges regularly improves problem-solving skills.",
        TextType.TEXT,
    ),
]

image_nodes = [
    TextNode(
        "Here's the Boot.dev logo: ![Boot.dev Logo](https://www.boot.dev/img/logo.png)",
        TextType.TEXT,
    ),
    TextNode(
        "Look at this cute dog: ![Cute Dog](https://images.unsplash.com/photo-1601758123927-1961d9ab264b)",
        TextType.TEXT,
    )
]