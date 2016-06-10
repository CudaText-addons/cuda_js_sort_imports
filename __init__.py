from cudatext import *
import sys
import os

from .sort_js_imports import sort_js_imports
from . import format_proc

format_proc.INI = 'a.ini'
format_proc.MSG = '[JS Sort Imports] '

def do_format(text):
    lines = text.splitlines()
    lines = sort_js_imports(lines)
    return '\n'.join(lines)

class Command:
    def config_global(self):
        format_proc.config_global()

    def config_local(self):
        format_proc.config_local()

    def run(self):
        format_proc.run(do_format)
