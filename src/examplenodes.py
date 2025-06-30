from textnode import TextNode, TextType

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