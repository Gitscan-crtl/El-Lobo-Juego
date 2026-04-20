import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
# En la sección de extensions:
extensions = [
 'sphinx.ext.autodoc',
 'sphinx.ext.napoleon',
 'sphinx_markdown_builder'
]

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'El-Lobo-Juego'
copyright = '2026, Anibal'
author = 'Anibal'
release = '20/4/26'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'spanish'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
