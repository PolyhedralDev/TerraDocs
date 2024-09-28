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
# sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath("./ext"))

# -- Project information -----------------------------------------------------

project = 'Terra'
copyright = '2021-2023, Terra Contributors'
author = 'Terra Contributors'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'jdlinker',
    'm2r2',
    'sphinx_design',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'configdocumenter',
    'platformversionsdocumenter',
]

source_suffix = [
    '.rst',
    '.md',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**/README.md']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

html_theme_options = {
    "dark_css_variables": {
        "color-foreground-primary": "#ffffff",
        "color-foreground-secondary": "#dbdbdb",
    },
    "light_css_variables": {
        "color-admonition-title--important": "#ff9100",
        "color-admonition-title-background--important": "rgba(255,145,0,.1)",
        "color-foreground-primary": "#000000",
        "color-foreground-secondary": "#333333",

        "font-stack": "-apple-system, BlinkMacSystemFont, Segoe UI, Cantarell, Roboto, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol",
        "admonition-font-size": "1rem",
    }
}

html_favicon = '../theme/favicon.ico'

html_logo = 'img/terra-logo.png'
html_title = 'Terra Docs'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [
    '../theme'
]

html_css_files = [
    'css/rounded-borders.css',
    'css/cards.css',
    'css/code-blocks.css',
    'css/interpreted-text.css',
    'css/padding.css',
    'css/headings.css',
    'css/admonitions.css',
    'css/tabs.css',
    'css/logo.css',
    'css/content.css',
    'css/lists.css',
    'css/text-colors.css',
]

# JDLinker config
javadoc_links = {
    'https://docs.oracle.com/en/java/javase/17/docs/api/java.base/': ['java'],
    'https://ci.codemc.io/job/PolyhedralDev/job/Terra/javadoc/': ['com.dfsek.terra'],
    'https://ci.codemc.io/job/PolyhedralDev/job/Tectonic/javadoc/': ['com.dfsek.tectonic'],
    'https://www.slf4j.org/apidocs/': ['org.slf4j'],
}

# Syntax Highlighting Color
pygments_style = 'stata-dark'
pygments_dark_style = 'stata-dark'

# Graphviz
graphviz_output_format = 'svg'
graphviz_dot_args = [
    '-Gpad=0.2',
]

# The master toctree document.
master_doc = 'index'
