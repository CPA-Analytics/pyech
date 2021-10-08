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
import os
import sys
import sphinx_bootstrap_theme
import sphinx_autodoc_typehints
from shutil import copyfile

sys.path.insert(0, os.path.abspath("../../"))
from pyech._version import __version__

copyfile("../../README.md", "README.md")


# -- Project information -----------------------------------------------------

project = 'pyech'
copyright = '2021, CPA Ferrere | Data Analytics'
author = 'CPA Ferrere | Data Analytics'

# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx.ext.viewcode", "recommonmark",
              "sphinx_toolbox.more_autodoc.typehints"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "bootstrap"
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_logo = "_static/pyech.png"
html_theme_options = {"navbar_title": " ",
                      "navbar_site_name": "Sections",
                      "bootswatch_theme": "flatly"}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

autodoc_member_order = "bysource"
add_function_parentheses = True
pygments_style = "sphinx"
master_doc = "index"
source_suffix = [".rst", ".md"]



autodoc_typehints = "description"