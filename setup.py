# evdschat - An open-source Python package for enhanced data retrieval.
# Copyright (c) 2024 Sermet Pekin
# Licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://creativecommons.org/licenses/by-nc/4.0/
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext

class BuildExt(build_ext):
    def build_extensions(self):
        super().build_extensions()

setup(
    name='evdschat',
    version='0.0.4',
    author='Sermet Pekin <sermet.pekin@gmail.com>',
    license='CC BY-NC 4.0',
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
