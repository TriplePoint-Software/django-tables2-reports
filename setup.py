# -*- coding: utf-8 -*-
# Copyright (c) 2016 by Max Syabro <maxim@syabro.com>
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

import os
from setuptools import setup, find_packages

__version__ = "0.0.12"


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name="tp-django-tables2-reports",
    version=__version__,
    author="Max Syabro",
    author_email="maxim@syabro.com",
    description="With django-tables2-reports you can get a report (CSV, XLS) of any django-tables2 with minimal changes to your project. Fork of abondened https://github.com/goinnn/django-tables2-reports",
    long_description=(read('README.rst') + '\n\n' + read('CHANGES.rst')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    license="LGPL 3",
    keywords="django,tables,django-tables2,reports,CSV,XLS",
    url='https://github.com/TriplePoint-Software/django-tables2-reports',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
