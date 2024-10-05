# tree-unfumbler
Python project for identifying code duplication issues in PN² v1.5 and perhaps attempting to alleviate them.

## How to run

### Prerequisites

- Python 3.12.
- Access to test-cliffhanger-prerefactor repo.
- Proven lack of skill issues in conflict resolution and codebase organization.

#### `python -m venv ./.venv`
#### `. ./.venv/bin/activate` (Linux/UNIX/macOS?) | `.\.venv\bin\activate.ps1` (Win) 
#### `cd app`

#### `python main.py`

## The master plan pipeline

- [x] Implement a to_string() tree printing method within Tree/Node_t.
- [ ] Convert Path dir tree to Tree/Node_t object.
- [ ] Impl. breadth first search for finding duplicate file/directory names.
- [ ] Identify duplicate name files and log them.
- [ ] Integrate with argparse for ease of use.
- [ ] Let user select what was found.
- [ ] Pick a duplicate file name from path Tree and print its [diffs](https://docs.python.org/3/library/difflib.html).
- [ ] Save diffs to a file, e.g. a Google Sheet for ease of analyzing.
- [ ] [automate this]