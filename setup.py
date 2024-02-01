from setuptools import find_packages, setup

setup(
      name='sppq',
      packages=find_packages(),
      version='0.1.2',
      description='I need this',
      author='SPPQ',
      setup_requires=['pytest-runner', 'g4f', 'requests', 'regex', 'bs4', 'asyncio'],
      tests_require=['pytest==4.4.1'],
      test_suite='tests',
)