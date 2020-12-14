"""This file helps to publish the module."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Vamsee",
    version="0.1.1",
    author="Vamsee Achanta",
    author_email="vamsee.achanta@aceengineer.com",
    description="TBA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="tba",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
