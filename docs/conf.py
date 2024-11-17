import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'sum.py'
copyright = '2024, issa'
author = 'issa'

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
html_static_path = ['_static']
