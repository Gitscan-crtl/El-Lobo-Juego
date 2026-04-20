# Al principio del archivo:
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
# En la sección de extensions:
extensions = [
 'sphinx.ext.autodoc',
 'sphinx.ext.napoleon',
 'sphinx_markdown_builder'
]