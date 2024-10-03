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

- [ ] save tree in Tree object
- [ ] save path Tree to a file
- [ ] identify duplicate name files
- [ ] pick a duplicate file name from path Tree and print its [diffs](https://docs.python.org/3/library/difflib.html)
- [ ] Save diffs to a file, e.g. a Google Sheet for ease of analyzing.
- [ ] automate this