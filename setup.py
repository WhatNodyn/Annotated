from setuptools import setup
from os import path

# Get long description from README
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='annotated',
    version='0.0.2',

    description='Apply annotations as callables on their respective arguments',
    long_description=long_description,

    url='https://github.com/WhatNodyn/Annotate',
    author='Neil Cecchini',
    author_email='stranger.neil@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3 :: Only',

        'License :: OSI Approved :: MIT License'
    ],

    keywords='annotations decorator function development',
    packages=['annotated']
)
