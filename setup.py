__version__ = '0.2'

import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid_formish',
    ]

if sys.version_info[:2] < (2,5):
    requires.append('uuid')

setup(name='pyramid_uniform',
      version=__version__,
      description='uni-form templates for pyramid_formish',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        ],
      keywords='web formish formgen pyramid',
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      author="Daniel Holth",
      author_email="dholth@fastmail.fm",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require=requires + ['nose'],
      install_requires=requires,
      entry_points="""\
      """
      )

