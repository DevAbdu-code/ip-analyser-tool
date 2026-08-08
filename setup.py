#!/usr/bin/env python3
"""
Setup script for IP Intelligence Tool
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ip-analyser-tool",
    version="2.0.0",
    author="Abdu (DevAbdu-code)",
    author_email="",
    description="Comprehensive IP address analysis and intelligence gathering tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DevAbdu-code/ip-analyser-tool",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC BY-ND 4.0",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Networking",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "python-whois>=0.8.0",
        "dnspython>=2.4.2",
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "ip-analyser=ip_analyser:main",
        ],
    },
)
