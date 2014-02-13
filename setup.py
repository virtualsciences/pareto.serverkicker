from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='vs.serverkicker',
      version=version,
      description="Checks for server availability, (re)starts if appropriate.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Guido Wesdorp',
      author_email='guido.wesdorp@vs.nl',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      namespace_packages=['vs', ],
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
        'console_scripts':
            'serverkicker = vs.serverkicker.serverkicker:command',
      },
  )
