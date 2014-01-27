from distutils.core import setup
from setuptools import find_packages

setup(name='djeventstream', 
      version='0.0',
      package_dir={'djeventstream.snshandler' : 'src/snshandler',
                   'djeventstream.httphandler' : 'src/httphandler', 
                   'djeventstream.httpbulkhandler' : 'src/httpbulkhandler', 
                   'djeventstream' : 'src/djeventstream'}, 
      packages=['djeventstream', 'djeventstream.snshandler', 'djeventstream.httphandler', 'djeventstream.httpbulkhandler'],
      author="Piotr Mitros", 
      license="AGPLv3, see LICENSE.txt")
