# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
from datetime import date

project = 'MoDyPy Documentation'
copyright = f"{date.today().year}, Ralf Gerlich"
author = 'Ralf Gerlich'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates", "modypy-sphinx-style/_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['venv', '_build', 'Thumbs.db', '.DS_Store', 'README.rst']


# -- Options for HTML output -------------------------------------------------


html_theme = "sphinx_rtd_theme"

html_static_path = ["modypy-sphinx-style/_static"]

# Logo and Favicon configuration
html_logo = "modypy-sphinx-style/_static/logo.svg"
html_favicon = "modypy-sphinx-style/_static/logo.ico"

html_context = {
    'deployment': True,
    'static_url': "https://docs.modypy.org/",
}
html_css_files = ["modypy.css"]
tags.add("deployment")

html_extra_path = [".htaccess"]
