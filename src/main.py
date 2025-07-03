import os
import shutil
from splitblocks import *
import sys

def main():
    root = "/home/hekkort/workspace/github.com/hekkort/ozmor"
    template_path = root + "/template.html"
    dest_path = root + "/public"
    src = root + "/static"
    content = root + "/content"

    basepath = sys.argv[0]
    if basepath == "":
        basepath = "/"

    copy(src, dest_path)

    generate_pages_recursive(content, template_path, dest_path, basepath)





def copy(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    items = os.listdir(src)
    for item in items:
        if os.path.isfile(os.path.join(src, item)):
            print(f"Copying file: {os.path.join(src, item)}")
            shutil.copy(os.path.join(src, item), dst)
        elif os.path.isdir(os.path.join(src, item)):
            print(f"Copying directory: {os.path.join(src, item)}")
            os.mkdir(os.path.join(dst, item))
            copy(os.path.join(src, item), os.path.join(dst, item))

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            if re.match(r"^(# )", block):
                block = block.lstrip("# ")
                return block.strip()
    raise Exception("no h1 header found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_contents = ""
    html_template = ""
    with open(from_path, "r") as file:
        md_contents = file.read()

    with open(template_path, "r") as file:
        html_template = file.read()
    
    html_string = markdown_to_html_node(md_contents)
    html_string = html_string.to_html()
    title = extract_title(md_contents)
    html_template = html_template.replace("{{ Title }}", title)
    html_template = html_template.replace("{{ Content }}", html_string)
    html_template = html_template.replace('href="/', f'href="{basepath}')
    html_template = html_template.replace('src="/', f'src="{basepath}')

    with open(dest_path + "/index.html", "w") as file:
        file.write(html_template)

    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    items = os.listdir(dir_path_content)

    for item in items:
        if item.endswith(".md"):
            print(f"src path: {os.path.join(dir_path_content, item)}")
            generate_page(os.path.join(dir_path_content, item), template_path, dest_dir_path, basepath)
        elif os.path.isdir(os.path.join(dir_path_content, item)):
            os.mkdir(os.path.join(dest_dir_path, item))
            print(f"dst path: {os.path.join(dest_dir_path, item)}")
            generate_pages_recursive(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item), basepath)
            
            



    

main()