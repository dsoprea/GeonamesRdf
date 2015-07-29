import os.path
import setuptools

import geonames

_APP_PATH = os.path.dirname(geonames.__file__)

with open(os.path.join(_APP_PATH, 'resources', 'README.rst')) as f:
      long_description = f.read()

with open(os.path.join(_APP_PATH, 'resources', 'requirements.txt')) as f:
      install_requires = list(map(lambda s: s.strip(), f.readlines()))

setuptools.setup(
    name='geonames_rdf',
    version=geonames.__version__,
    description="Query data from geonames.org and return RDF/Semantic Web data.",
    long_description=long_description,
    classifiers=[],
    keywords='geonames rdf',
    author='Dustin Oprea',
    author_email='myselfasunder@gmail.com',
    url='https://github.com/dsoprea/PathManifest',
    license='GPL 2',
    packages=setuptools.find_packages(exclude=['dev']),
    include_package_data=True,
    zip_safe=False,
    package_data={
        'geonames': [
            'resources/README.rst',
            'resources/requirements.txt'
        ],
    },
    install_requires=install_requires,
    scripts=[
          'geonames/resources/scripts/gn_search',
    ],
)
