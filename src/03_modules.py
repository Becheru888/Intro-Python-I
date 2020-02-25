"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

arg_list = sys.argv

for arg in arg_list:
    print(str(arg) + '\n')

# Print out the OS platform you're using:
# YOUR CODE HERE

from sys import platform

if platform == 'linux':
    print('Linux')
elif platform == 'darwin':
    print('OS')
elif platform == 'win32':
    print('Windows')

# Print out the version of Python you're using:
# YOUR CODE HERE

import platform

print("Python version is", platform.python_version())

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE

print(os.getcwd())


import getpass
# Print out your machine's login name
# YOUR CODE HERE

print(getpass.getuser())

