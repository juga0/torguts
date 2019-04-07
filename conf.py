# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_bootstrap_theme

# -- Project information -----------------------------------------------------

# This variables should be parsed and not hard coded.
# As well as version.
project = 'Tor codebase additional'
copyright = '2019, The Tor Project'
author = 'The Tor Project'
# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['requirements.txt']

source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Use bootstrap because torproject.org uses bootstrap.
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_logo = "_static/tor-logo.svg"
# From https://bootswatch.com/3/
html_theme_options = {
    'bootswatch_theme': "flatly",
}
# bootstrap could be replaced by a custom theme for all the documentation
# created with Sphinx, see # http://www.sphinx-doc.org/en/master/theming.html.
# Sphinx uses Jinja engine, same as lektor, so it seems not difficult not to
# base it on https://gitweb.torproject.org/project/web/template.git.
# If the directory templates and static are just copied in this project
# static and templates files respectively, make html fails:
# Reason: TemplateAssertionError("no filter named 'asseturl'",)
