"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

from kirk import __version__ as version
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kirk-python-sdk',  # Required
    version=version,  # Required
    description='Qiniu Kirk Python SDK',  # Required
    long_description=long_description,  # Optional
    url='https://github.com/qiniu/kirk-python-sdk',  # Optional
    author='cairo',  # Optional
    author_email='shuimuliang@gmail.com',  # Optional

    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords=('qiniu kirk sdk'),  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    install_requires=['requests'],  # Optional

    setup_requires=['setuptools'],
    test_suite='tests',
)
