#! /usr/bin/env python3

from setuptools import setup

url = "https://github.com/chuanconggao/RegexOrder"
version = "0.2"

setup(
    name="RegexOrder",

    packages=["regexorder"],
    include_package_data=True,

    url=url,

    version=version,
    download_url=f"{url}/tarball/{version}",

    license="MIT",

    author="Chuancong Gao",
    author_email="chuancong@gmail.com",

    description="Search the regex that fits all querying strings.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",

    keywords=[
        "regex",
        "string-matching"
        "partial-order"
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
    ],

    python_requires=">= 3",
    install_requires=[
        line.strip() for line in open("requirements.txt")
    ]
)
