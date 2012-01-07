#
#   Copyright [2011] [Patrick Ancillotti]
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import os
import sys

from setuptools import setup, find_packages
from distutils.core import Command
from subprocess import call


class Pep8Command(Command):
    description = "run pep8 script"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            import pep8
            pep8
        except ImportError:
            print 'Missing "pep8" library. You can install it using pip: ' + \
                    'pip install pep8'
            sys.exit(1)

        cwd = os.getcwd()
        retcode = call(('pep8 %s/Moonshine/ %s/test/' % (cwd, cwd)).split(' '))
        sys.exit(retcode)


setup(name='Moonshine',
        version=__import__('Moonshine').__version__,
        description='Virtual Image Distribution Through BitTorrent',
        long_description=''' ''',
        classifiers=[],
        keywords='',
        author='Patrick Ancillotti',
        author_email='patrick@eefy.net',
        url='http://www.github.com/neogenix/Moonshine',
        license='LICENSE',
        packages=find_packages(
            exclude=[
                'ez_setup',
                'examples',
                'tests'
            ]
        ),
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'requests',
            'anyjson'
        ],
        data_files=[
            ('/etc/Moonshine', ['Moonshine.conf'])
        ],
        entry_points={
            'console_scripts':
                ['Moonshine = Moonshine:main']
        },
        cmdclass={
            'pep8': Pep8Command
        }
)
