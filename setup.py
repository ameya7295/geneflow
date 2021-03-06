# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from time import time
from setuptools import setup
from setuptools import find_packages

long_description = open("README.md").read()
version = '0.3.%s' % int(time())

setup(name='geneflow',
      version=version,
      description='Genetic Algorithm for humans',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Elie Bursztein',
      author_email='elieb@google.com',
      url='https://github.com/google/geneflow',
      license='Apache 2',
      package_data={"": ["*.json"]},
      install_requires=[
          'networkx', 'numpy', 'tqdm', 'tabulate', 'termcolor', 'matplotlib',
          'plotly', 'pandas'
      ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers', 'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=find_packages())
