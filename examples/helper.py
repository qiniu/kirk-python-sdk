import os
import os.path
import sys

def get_codebase_dir():
    d = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.append(d)

get_codebase_dir()
