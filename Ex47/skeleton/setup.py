try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup 
    
config = [
    'description': 'My Project',
    'author': 'KSH',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'yocson@outlook.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'scripts': [],
    'name': 'projectname'
]

setup(**config)