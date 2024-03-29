from setuptools import setup, find_packages
import os

version = '1.2'

setup(name='transmogrify.command',
      version=version,
      description="transmogrifier blueprint to pipe keys via a shell command",
      long_description=open('README.rst').read() +'\n'+
#                       open(os.path.join("transmogrify", "siteanalyser", "isindex.txt")).read() + "\n" +
#                       open(os.path.join("transmogrify", "siteanalyser", "relinker.txt")).read() + "\n" +
#                       open(os.path.join("transmogrify", "siteanalyser", "makeattachments.txt")).read() + "\n" +
                       #open(os.path.join("transmogrify", "siteanalyser", "backlinkstitle.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='transmogrifier blueprint funnelweb',
      author='Dylan Jay',
      author_email='software@pretaweb.com',
      url='http://github.com/collective/transmogrify.command',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['transmogrify'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.transmogrifier',
          ],
      entry_points="""
            [z3c.autoinclude.plugin]
            target = transmogrify
            """,
            )
