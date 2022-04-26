try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

#requirements = ["feedparser", "jinja2", "mutagen", "click", "keyring", "requests"]

config = {
    'description': 'My project',
    'author': 'Dunming Hua',
    'url': 'URL to get it at.',
    'download_url': 'where to download it',
    'author_email': 'dunminghua@163.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'NAME'
    'classifiers': [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
    ]
}

setup(**config)

