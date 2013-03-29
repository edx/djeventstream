from distutils.core import setup
from setuptools import find_packages

setup(name='djeventstream', 
      version='0.0',
      package_dir={'djeventstream.snshandler' : 'src/snshandler',
                   'djeventstream.httphandler' : 'src/httphandler', 
                   'djeventstream' : 'src/djeventstream'}, 
      packages=['djeventstream', 'djeventstream.snshandler', 'djeventstream.httphandler'],
      author="Piotr Mitros", 
      license="AGPLv3, see LICENSE.txt")
