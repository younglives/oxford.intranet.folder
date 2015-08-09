from setuptools import setup, find_packages
import os

version_path = os.path.join("oxford", "intranet", "folder", "version.txt")

version = open(version_path).read().strip()

long_description = open(os.path.join("README.md")).read()
long_description += "\n" + open(os.path.join("docs", "INSTALL.txt")).read()
long_description += "\n" + open(os.path.join("docs", "HISTORY.txt")).read()

setup(
    name='oxford.intranet.folder',
    version=version,
    description="",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
    keywords='',
    author='',
    author_email='',
    url='http://svn.plone.org/svn/collective/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['oxford', 'oxford.intranet'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools', ],
    extras_require={
        'test': [
            'plone.app.testing',
        ]
    },
    entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
    )
