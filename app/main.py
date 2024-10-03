# tree-unfumbler
# For Project Nitrox² revival undertaking, made with hope and pure unadulterated 'tism 
#
################
#
# main.py
#
import argparse
import difflib
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


    def to_string(self, parent_depth=None, depth=0, prefix="") -> str:
        p: str = prefix
        tree_str: str = self.filename

        parent_depth = depth - 1 if depth != 0 else None
        depth_tuple = " " + str(tuple((parent_depth, depth)))

        tpf_space = ' ' * 4
        tpf_branch = '|' + ' ' * 3
        tpf_leaf = '├── '
        tpf_lastleaf = '└── '
        tree_prefixes = list()
        subdirs = list(root_dir.iterdir())
        tree_prefixes = [tpf_leaf] * (len(subdirs) - 1) + [tpf_lastleaf]

        if self.filetype == "/" and self.children != None:
            tree_str = self.filename + "/" + depth_tuple + '\n'
            tree_str = (tpf_lastleaf if parent_depth == None else tpf_space + tpf_leaf) + tree_str
            for child in self.children:
                tree_str = tree_str + child.to_string(depth=depth+1, prefix=p)
            return tree_str
        elif self.filetype == "/" and self.children == None:
            tree_str = self.filename + "/"
            # if depth >= parent_depth:
            #     p = p + tpf_space
            #     tree_str = tpf_space + tpf_leaf + tree_str
            return tree_str + depth_tuple + '\n'
        else:
            tree_str = self.filename + "." + self.filetype
            if depth >= parent_depth:
                p = p + tpf_space
                tree_str = tpf_space + tpf_leaf + tree_str
            return p + tree_str + depth_tuple + '\n'


def get_pafway() -> Path:
    pafway = None

    with open("./pafway.txt", "r") as pafway_file:
        pafway = pafway_file.read()
        pafway = pafway.strip('\n')

    pafway_file.close()
    return Path(pafway) # toeden


# print pretty tree - https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
def print_pathtree(dir_path: Path, prefix: str=''):
    subdirs = list(dir_path.iterdir())

    tpf_space = ' ' * 4
    tpf_branch = '|' + ' ' * 3
    tpf_leaf = '├── '
    tpf_lastleaf = '└── '
    
    tree_prefixes = [tpf_leaf] * (len(subdirs) - 1) + [tpf_lastleaf]
    for tree_prefix, path in zip(tree_prefixes, subdirs):
        yield prefix + tree_prefix + path.name
        # Extend the prefix and recurse:
        if path.is_dir(): 
            extension = tpf_branch if tree_prefix == tpf_leaf else tpf_space
            yield from print_pathtree(path, prefix=prefix+extension)


def path_to_tree(dir_path: Path):
    subdirs = list(dir_path.iterdir())

    dir_tree = Tree("cliffhanger_rev7/src", "/")
    for path in subdirs:
        yield path.name
        tree.add_child()   
        # Extend the prefix and recurse:
        if path.is_dir(): 
            yield from path_to_tree(path)


if __name__ == "__main__":
    file11 = Tree("something", "lua")
    file12 = Tree("chicane_car_vroom", "lua")
    dir1 = Tree("directory", "/", [file11, file12])

    file21 = Tree("button", "lua")
    file22 = Tree("whatever", "json")
    dir21 = Tree("subdir", "/", [file21, file22, file12])
    dir2 = Tree("directory_2", "/", [file21, file22, dir21])

    dir3 = Tree("enmpty", "/")
    file_alone = Tree("lonelyscript", "lua")

    parent_tree = Tree("", "/", [dir1, dir2, file_alone, dir3])
    print(parent_tree.to_string())
    # for line in print_pathtree(get_pafway()):
    #     print(line)
    

####### Copyleft LVSA 09-10.2024
# Terms of use:
# 1. Be competent, especially if you're over 32.
# 2. Don't steal 1.3k$ from your close ones.
