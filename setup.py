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
      install_requires=[
          'g4f',
          'requests',
          'asciitext',
          'tqdm',
          'discord_webhook',
          'matplotlib',
          'colorama'
      ],
      python_requires='>=3.9',
      test_suite='tests',
)