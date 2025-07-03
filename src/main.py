import os
import shutil
from splitblocks import *

def main():
    src = "/home/hekkort/workspace/github.com/hekkort/ozmor/static"
    dst = "/home/hekkort/workspace/github.com/hekkort/ozmor/public"
    copy(src, dst)


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
    pass
    

main()