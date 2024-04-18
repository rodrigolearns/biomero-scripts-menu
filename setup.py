#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 University of Dundee.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Aleksandra Tarkowska <A(dot)Tarkowska(at)dundee(dot)ac(dot)uk>,
#
# Version: 1.0

import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = '0.0.1.dev0'


setup(name="BiomeroScriptsMenu",
      packages=find_packages(exclude=['ez_setup']),
      version=VERSION,
      description="Biomero scripts menu plugin for OMERO.web",
      long_description=read('README.rst'),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: JavaScript',
          'Programming Language :: Python :: 3',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Internet :: WWW/HTTP :: WSGI',
          'Topic :: Scientific/Engineering :: Visualization',
          'Topic :: Software Development :: Libraries :: '
          'Application Frameworks',
          'Topic :: Software Development :: Testing',
          'Topic :: Text Processing :: Markup :: HTML'
      ],
      author='Rodrigo Rosas-Bertolini',
      author_email='r.rosas@amsterdamumc.nl',
      license='AGPL-3.0',
      url="https://github.com/rodrigolearns/biomero-scripts-menu.git",
      download_url='https://github.com/rodrigolearns/biomero-scripts-menu/archive/v%s.tar.gz' % VERSION,
      keywords=['OMERO.web', 'plugin'],
      install_requires=['omero-web>=5.6.0'],
      python_requires='>=3',
      include_package_data=True,
      zip_safe=False,
      )
