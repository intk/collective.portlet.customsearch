from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(name='collective.portlet.customsearch',
      version=version,
      description="Custom search portlet.",
      long_description=open("README.rst").read() + "\n" +
                       open("docs/HISTORY.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='search',
      author='Andre Goncalves',
      author_email='andre@intk.com',
      url='https://github.com/intk/collective.portlet.customsearch',
      download_url='https://github.com/intk/collective.portlet.customsearch/tarball/0.0.1',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.portlet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
