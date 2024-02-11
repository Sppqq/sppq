from setuptools import find_packages, setup
import re

v = open('sppq/__init__.py', 'r').read()

match = re.search(r"__version__ = '(.*)'", v)
if match:
    version = match.group(1)

setup(
      name='Sppq',
      packages=find_packages(),
      version=version,
      description='Library with many functions',
      author='SPPQ',
      setup_requires=['pytest-runner', 'g4f', 'requests', 'regex', 'bs4', 'asyncio', 'asciitext'],
      tests_require=['pytest==4.4.1', 'pytest-runner', 'g4f', 'requests', 'regex', 'bs4', 'asyncio', 'asciitext'],
      test_suite='tests',
)