from setuptools import setup, find_packages

setup(
    name="sppq",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "asciitext>=1.1.1",
        "tqdm>=4.66.1",
        "discord-webhook>=1.3.0",
        "matplotlib>=3.8.0",
        "colorama>=0.4.6",
    ],
    python_requires=">=3.9",
    author="sppq",
    description="Utility library for various functions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sppq/sppq",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)