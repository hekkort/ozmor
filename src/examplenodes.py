from textnode import TextNode, TextType

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