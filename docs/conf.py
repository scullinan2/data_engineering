# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys, os

#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#sys.path.insert(0, os.path.abspath(".."))
#sys.path.insert(0, os.path.abspath(os.path.join('..', '..', 'sources')))
#basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
#sys.path.insert(0, basedir)
#sys.path.insert(0, os.path.abspath('../sources'))
#sys.path.append(os.path.join(os.path.dirname(__file__)))
#print(sys.path)
#sys.path.append('..')
sys.path.insert(0, os.path.abspath('../data_loaders')) 

project = "shane's data loaders"
copyright = '2023, shane'
author = 'shane'
release = '0.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
