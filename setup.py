import re
from os.path import join, dirname
from setuptools import setup, find_packages


# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), 'restfulpy_boilerplate', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)


dependencies = [
    'restfulpy >= 0.42.0',

    # deployment
    'gunicorn',

    # testing
    'requests',
    'webtest',
    'bddrest'
]


setup(
    name="restfulpy-boilerplate",
    version=package_version,
    author="Seyyed Mohammad Borghei",
    author_email="memlucky@carrene.com",
    description="An empty restfulpy project",
    url='https://github.com/Carrene/restfulpy-boilerplate.git',
    install_requires=dependencies,
    packages=find_packages(),
    test_suite="restfulpy-boilerplate.tests",
    entry_points={
        'console_scripts': [
            'restfulpy-boilerplate = restfulpy_boilerplate:restfulpy_boilerplate.cli_main'
        ]
    },
    message_extractors={'restfulpy-boilerplate': [
        ('**.py', 'python', None),
    ]},
)
