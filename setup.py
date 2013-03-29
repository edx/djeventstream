from distutils.core import setup
from setuptools import find_packages

setup(name='djeventstream', 
      version='0.0',
      package_dir={'djeventstream': 'src'}, 
      packages=find_packages('src'),
      author="Piotr Mitros", 
      license="AGPLv3, see LICENSE.txt")
