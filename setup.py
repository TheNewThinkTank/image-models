#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

test_requirements = [
    "pytest>=3",
]

setup(
    author="Gustav Collin Rasmussen",
    author_email="gcr84@hotmail.com",
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="multiclass image ML models to classify images of varying types",
    entry_points={
        "console_scripts": [
            "image_models=image_models.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="image_models",
    name="image_models",
    packages=find_packages(include=["image_models", "image_models.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/TheNewThinkTank/image_models",
    version="0.1.0",
    zip_safe=False,
)
