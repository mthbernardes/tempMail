# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='tempMail',
    version='1.0',
    url='https://github.com/mthbernardes/tempMail',
    license='MIT License',
    author='Matheus Bernardes',
    author_email='mthbernardes@gmail.com',
    keywords='email temporary',
    description=u'Module to generate an temporary e-mail',
    packages=['tempMail'],
    install_requires=['requests','lxml'],
)
