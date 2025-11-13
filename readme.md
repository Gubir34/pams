PyAppMS - Python Application Management System

PyAppMS is a lightweight Python CLI tool that allows you to install and run Python applications directly from GitHub repositories.

# Features

Search GitHub for a program by name.

Automatically clone or update the repository.

Detect the main Python file from pams.txt or use main.py by default.

Display installation progress in the terminal.

Standardize folder names (e.g., "Ltf Editor" → ltf_editor).

# Installation

Install PyAppMS via pip:

pip install pyappms --break-system-packages

# Usage

To install and run a program:

pyappms install <program_name>

## Example:

pyappms install ltf_editor

# Output:

----Python Application Management System----
Installing ltf_editor...

###################------------------------ 50% Installing ltf_editor...

################################################## 100% Installing ltf_editor...
Installation complete!

If the GitHub repo contains pams.txt, PyAppMS uses the mainfile defined in it.
If pams.txt does not exist, it defaults to main.py.

 # Requirements

Python 3.7+

Packages: requests, gitpython

Install dependencies manually (if needed):

pip install gitpython requests --break-system-packages

# License

This project is licensed under the MIT License. See the LICENSE file for details.
