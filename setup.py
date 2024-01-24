from setuptools import setup, find_packages



# Note: keep requirements here to ease distributions packaging
tests_require = []
dev_require = []
install_requires = [
    'pip',
    'setuptools',
    'g4f',
]
install_requires_win_only = []


setup(
    name='Sppq',
    version='1.0',
    description='None',
    long_description='',
    long_description_content_type='text/markdown',
    url='https://github.com/Sppqq/sppq',
    download_url=f'https://github.com/Sppqq/sppq',
    author='Sppq',
    author_email='sppqq@duck.com',
    license='None',
    packages=find_packages(include=['httpie', 'httpie.*']),
    entry_points={},
    python_requires='>=3.7',
    install_requires=install_requires,
    classifiers=[],
    project_urls={
        'GitHub': 'https://github.com/Sppqq/sppq'
    },
    data_files=[]
)