# tree-unfumbler
# For Project Nitrox² revival undertaking, made with hope and pure unadulterated 'tism 
#
################
#
# main.py
#
import argparse
from pathlib import Path


type Node_t = Tree()


class Tree(object):
    def __init__(self, filename=None, filetype=None, children=None):
        self.filename: str = filename 
        self.filetype: str = filetype
        self.children: list[Node_t] = list() 
        if children is not None:
            for child in children:
                self.add_child(child)
    

    def add_child(self, child: Node_t):
        assert isinstance(child, Tree)
        self.children.append(child)


    def to_string(self) -> str:
        if self.filetype == "/":
            if self.children != None:
                tree_str: str = self.filename + "/"
                for child in self.children:
                    tree_str = tree_str + child.to_string()
                return tree_str

            return str(self.filename + "/")

        return str(self.filename + "." + self.filetype)


if __name__ == "__main__":
    print("let's go")
    tree = Tree("somescript", "lua")
    print(tree.to_string())
    tree2 = Tree("directory", "/")
    print(tree2.to_string())
    tree2.add_child(tree)
    print(tree2.to_string())

####### Copyleft LVSA 09.2024
# Terms of use:
# 1. Be competent, especially if you're over 32.
# 2. Don't steal 1.3k$ from your close ones.
