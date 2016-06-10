Plugin for CudaText.
This is port of plugin for Sublime Text: https://github.com/insin/sublime-sort-javascript-imports

It sorts selected lines containing JavaScript import statements or require() calls by the module path they're importing.
Lines will be sorted based on the module path being imported, respecting (and normalising) any blank lines used to divide imports into different categories.
Any non-import lines in the selection will be moved to the end, separated by a new blank line if necessary.

Import ordering:
Where top-level imports and path-based imports are mixed in the same block, they will be ordered as follows:

    Top-level imports
    Imports which traverse up out of the current directory, from furthest away to closest
    Imports within the current directory

Note: if you're using Webpack aliases or a Babel alises plugin for top-level importing of your app's own code, you might want to put those in a separate block for clarity.


Ported by: Alexey T
