# -*- coding: utf-8 -*-
from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

packages = ['tickytacky']

package_data = {'': ['*']}

install_requires = ['pyglet>=1.5.23,<2.0.0']

setup_kwargs = {
    'name': 'tickytacky',
    'version': '0.5.0',
    'description': 'Tickytacky pixel game maker',
    'long_description': long_description,
    'author': 'JP Etcheber',
    'author_email': 'jetcheber@gmail.com',
    'url': 'https://github.com/numbertheory/tickytacky',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}

setup(**setup_kwargs)
