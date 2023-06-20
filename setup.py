from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='new file listener',
    version='0.1.0',
    description='Nucleai homework',
    long_description=readme,
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

