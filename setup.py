from distutils.core import setup
from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'pygates',       
  packages = ['pygates'],  
  version = '0.2',     
  license='MIT',      
  description = 'With PyGates library, you can use logic gates on Python.',  
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Batuhan Ergün',               
  author_email = 'contact@batuhanergun.com',      
  url = 'https://github.com/Baticaly/PyGates',  
  download_url = 'https://github.com/Baticaly/PyGates/archive/0.1.tar.gz',
  keywords = ['PyGates', 'Python', 'Conditionals'],  
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',    
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
