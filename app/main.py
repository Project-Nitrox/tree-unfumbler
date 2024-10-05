# tree-unfumbler
# For Project Nitrox² revival undertaking, made with hope and pure unadulterated 'tism 
#
################
#
# main.py
#
import argparse
import difflib
import os
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


    def to_string(self, prefix="") -> str:
        node_str: str = ""
        # extension = ""
        if self.filename == ".":
            node_str: str = self.filename + ("." + self.filetype if self.filetype != "/" else self.filetype) + '\n'
        
        tpf_space = ' ' * 4
        tpf_branch = '│' + ' ' * 3
        tpf_leaf = '├── '
        tpf_lastleaf = '└── '
        
        tree_prefixes = [tpf_leaf] * (len(self.children) - 1) + [tpf_lastleaf]
        for child, pref in zip(self.children, tree_prefixes):
            filetype = "." + child.filetype if child.filetype != "/" else child.filetype
            node_str += prefix + pref + child.filename + filetype + '\n'
            if len(child.children) > 0:
                extension = tpf_branch if pref == tpf_leaf else tpf_space
                node_str += child.to_string(prefix=prefix+extension)
        return node_str


def get_pafway() -> Path:
    pafway = None

    with open("./pafway.txt", "r") as pafway_file:
        pafway = pafway_file.read()
        pafway = pafway.strip('\n')

    pafway_file.close()
    return Path(pafway) # toeden


# print pretty tree - https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
def path_to_iter(dir_path: Path, prefix: str=''):
    subdirs = list(dir_path.iterdir())

    tpf_space = ' ' * 4
    tpf_branch = '│' + ' ' * 3
    tpf_leaf = '├── '
    tpf_lastleaf = '└── '
    
    tree_prefixes = [tpf_leaf] * (len(subdirs) - 1) + [tpf_lastleaf]
    for tree_prefix, path in zip(tree_prefixes, subdirs):
        yield prefix + tree_prefix + path.name
        # Extend the prefix and recurse:
        if path.is_dir(): 
            extension = tpf_branch if tree_prefix == tpf_leaf else tpf_space
            yield from path_to_iter(path, prefix=prefix+extension)


def path_to_tree(dir_path: Path):
    subdirs = list(dir_path.iterdir())

    # dir_tree = Tree("cliffhanger_rev7/src", "/")
    dir_tree = None
    if dir_path.is_dir():
        dir_tree = Tree(str(dir_path), "/")
    for path in subdirs:
        filetype = ("/" if path.is_dir() else (os.path.splitext(path)[1] if path.is_file() else "eror?"))
        print(os.path.splitext(path))
        dir_tree.add_child(Tree(str(path), filetype))
        
    print(dir_tree.children[3].filetype)
    #     yield path.name
    #     tree.add_child()   
    #     # Extend the prefix and recurse:
    #     if path.is_dir(): 
    #         yield from path_to_tree(path)


if __name__ == "__main__":
    file11 = Tree("something", "lua")
    file12 = Tree("chicane_car_vroom", "lua")
    dir1 = Tree("directory", "/", [file11, file12])

    file21 = Tree("button", "lua")
    file22 = Tree("whatever", "json")
    file211 = Tree("button", "lua")
    file212 = Tree("whatever", "/")
    file213 = Tree("chicane_car_vroom", "lua")
    dir2 = Tree("subdir", "/", [file211, file212, file213])
    dir3 = Tree("directory_2", "/", [file21, file22, dir2])

    dir4 = Tree("enmpty", "/")
    file_alone = Tree("lonelyscript", "lua")

    parent_tree = Tree(".", "/", [dir1, dir3, file_alone, dir4])
    print(parent_tree.to_string())
    for line in path_to_iter(get_pafway()):
        print(line)
    # path_to_tree(Path("./testdir"))
    

####### Copyleft LVSA 09-10.2024
# Terms of use:
# 1. Be competent, especially if you're over 32.
# 2. Don't steal 1.3k$ from your close ones.
