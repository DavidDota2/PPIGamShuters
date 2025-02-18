# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../../ui'))  # Указываем путь к корню проекта
sys.path.insert(0, os.path.abspath('../../characterSkripts')) 

project = 'PPiGameShuters'
copyright = '2025, David Podzol'
author = 'David Podzol'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # Автоматически вытягивает docstrings из кода
    'sphinx.ext.napoleon',  # Поддержка Google и NumPy стилей документации
    'sphinx.ext.viewcode',  # Добавляет ссылки на исходный код
]


templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
