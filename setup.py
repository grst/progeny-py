#!/usr/bin/env python

from distutils.core import setup
setup(
   name='progeny',
   version='1.0',
   description='PROGENy is a python package to compute pathway activity from RNA-seq data',
   author='Pau Badia i Mompel',
   url='https://github.com/saezlab/progeny-py',
   packages=['progeny'], 
   license='LICENSE.txt',
   package_data={'progeny': ['data/model_human_full.pkl', 'data/model_mouse_full.pkl']},
   install_requires=[
        'anndata',
        'scanpy',
        'numpy',
        'pandas',
        'tqdm'
   ]
)