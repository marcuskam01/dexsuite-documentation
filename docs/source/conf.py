# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Dexsuite'
copyright = '2025, motoko'
author = 'motoko'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

try:
   extensions
except NameError:
   extensions = []

extensions.append('sphinx_wagtail_theme')
html_theme = 'sphinx_wagtail_theme'

html_static_path = ['_static']
html_css_files = ["custom.css"]
html_show_sphinx = False
html_theme_options = dict(
    github_url = "https://github.com/marcuskam01/dexsuite-documentation/tree/main/docs",
    footer_links = ",".join([
        "About Us|https://www.mcgill.ca/cim/",
        "Repository|https://github.com/anashoussaini/Dexsuite"
    ]),
 )