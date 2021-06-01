from distutils.core import setup
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name = 'jagokata',        
  packages = ['jagokata'],   
  version = '0.0.2',    
  license='MIT',     
  description = 'JagoKata Scrapper, kata-bijak&peribahasa', 
  author = 'Krypton Byte',                  
  author_email = 'galaxyvplus6434@gmail.com',     
  url = 'https://github.com/krypton-byte/jagokata',   
  download_url = 'https://github.com/krypton-byte/jagokata/archive/0.0.2.tar.gz',    
  keywords = ['jagokata', 'peribahasa', 'kata-bijak', 'katabijak'], 
  install_requires=[           
          'bs4',
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)