
from setuptools import setup

setup_args = {'description': 'Testing...',
   'install_requires': ['juliapkg', 'juliacall'],
   'keywords': ['openmdao_component'],
   'license': 'MIT',
   'name': 'pyfoo',
   'packages': ['pyfoo'],
   'version': '0.1.0'}

setup(**setup_args)
