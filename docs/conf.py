# This file is covered by the LICENSE file in the root of this project.

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

import pkg_resources

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = "Novu SDK"
copyright = f"2023-{datetime.date.today().year}, Spikeelabs"  # pylint: disable=W0622
authors = [
    "Oscar MARIE--TAILLEFER <oscar.marie-taillefer@spikeelabs.fr>",
]

release = version = pkg_resources.get_distribution("novu").version
language = "en"

master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "m2r2",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
templates_path = ["_templates"]

# -- Options for napleon extensions ------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/dev/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/stable/", None),
    "requests": ("https://requests.readthedocs.io/en/latest/", None),
}

source_suffix = [".rst", ".md"]
