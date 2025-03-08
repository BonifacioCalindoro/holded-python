#!/usr/bin/env python
"""
Setup script for the Holded API wrapper.
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Define requirements directly instead of reading from requirements.txt
requirements = [
    "requests>=2.25.0",
    "aiohttp>=3.7.4",
    "python-dateutil>=2.8.2",
    "typing-extensions>=4.0.0",
    "pydantic>=2.0.0"
]

setup(
    name="holded-python",
    version="0.1.3",
    author="BonifacioCalindoro",
    author_email="marcos@marcosgimenez.tech",
    description="A comprehensive Python wrapper for the Holded API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BonifacioCalindoro/holded-python",
    packages=find_packages(include=["holded", "holded.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    keywords=["holded", "api", "wrapper", "client", "erp", "crm"],
    include_package_data=True,
) 