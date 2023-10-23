#0x15. API


# Introduction

An application program interface (API) is a set of routines, protocols, and tools for building software applications. Basically, an API specifies how software components should interact. Additionally, APIs are used when programming graphical user interface (GUI) components. A good API makes it easier to develop a program by providing all the building blocks. A programmer then puts the blocks together.

# Requirements

## Development Environment

- You are allowed to use the following text editors: vi, vim, emacs.
- All code will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5).
- All your source code files must end with a new line.
- The first line of every source code file must be exactly `#!/usr/bin/python3`.
- Libraries imported in your Python files must be organized in alphabetical order
- Your code should adhere to the PEP 8 style guide (Python Enhancement Proposal 8).
- We will use pycodestyle (version 2.8.*) to check for PEP 8 compliance.
- All your source code files must be executable (use `chmod +x`)
- The length of your source code files will be measured using the `wc` command.
- All modules in your project should have appropriate documentation.
- You can check this by running `python3 -c 'print(__import__("your_module").__doc__)'`.
- You must use the `get` method to access dictionary values by key. It should not throw an exception if the key doesn't exist in the dictionary.

## Entry Point

- Your code should not be executed when imported. Use the following convention to prevent execution when imported:

```python
if __name__ == "__main__":
    # Your main code here
```

# Files

- 0-gather_data_from_an_API.py : a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
- 1-export_to_CSV.py : Python script to export data in the JSON format.
- 3-dictionary_of_list_of_dictionaries.py : Python script to export data in the JSON format.
