from setuptools import find_packages, setup

setup(
      name='Sppq',
      packages=find_packages(),
      version='0.1.5',
      description='I need this',
      author='SPPQ',
      setup_requires=['pytest-runner', 'g4f', 'requests', 'regex', 'bs4', 'asyncio', 'asciitext'],
      tests_require=['pytest==4.4.1', 'pytest-runner', 'g4f', 'requests', 'regex', 'bs4', 'asyncio', 'asciitext'],
      test_suite='tests',
)