#!/usr/bin/env python
"""setup file."""
from sys import platform
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')  # NOQA
except ImportError:
    print(
        "warning: pypandoc module not "
        "found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()  # NOQA

setup(
    name='instantmusic',
    version='1.3.0',
    description=(
        'Instantly download any song! '
        'Without knowing the name of the song!!!!'),
    long_description=read_md('README.md'),
    author='Yask Srivastava',
    author_email='yask123@gmail.com',
    url='https://github.com/yask123/Instant-Music-Downloader',
    license='MIT',
    packages=['instantmusic'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'beautifulsoup4>=4.6.0',
        'eyeD3>=0.8',
        'requests>=2.14.2',
        'youtube-dl>=2017.5.14',
    ] + (['pyreadline'] if platform.startswith('win') else []),
    zip_safe=False,
    entry_points={'console_scripts': [
        'instantmusic = instantmusic.instantmusic:main'
    ]},
    keywords='instant music download',
)
