# evdschat - An open-source Python package for enhanced data retrieval.
# Copyright (c) 2024 Sermet Pekin
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext

class BuildExt(build_ext):
    def build_extensions(self):
        super().build_extensions()

setup(
    name='evdschat',
    version='0.0.4',
    author='Sermet Pekin <sermet.pekin@gmail.com>',
    license='MIT',
    packages=find_packages(),
    package_data={'evdschat': ['libpost_request.so']},
    cmdclass={'build_ext': BuildExt},
    ext_modules=[
        Extension(
            'evdschat.libpost_request',
            sources=['evdschat/src/getter.c'],
            libraries=['curl'],
        ),
    ],
    install_requires=[
        'evdspy'
    ],
    entry_points={
        'console_scripts': [
            'evdschat=evdschat.module:chat_console',
        ],
    },
)
