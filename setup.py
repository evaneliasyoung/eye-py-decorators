#!/usr/bin/env python3
"""
@file      setup.py
@brief     Setup PIP package.

@author    Evan Elias Young
@date      2022-02-22
@date      2022-02-22
@copyright Copyright 2022 Evan Elias Young. All rights reserved.
"""

from setuptools import setup, find_packages


if __name__ == "__main__":
    setup(
        name="eye-py-decorators",
        version="1.0.0",
        description="Decorators for Humans",
        author="Evan Elias Young",
        author_email="evanyoung762@gmail.com",
        url="https://github.com/evaneliasyoung/eye-py-decorators",
        license="GNU GPLv3",
        package_dir={"": "src"},
        py_modules=["eye_decorators"],
        keywords=["decorators", "generic", "utility"],
        platforms=["All"],
        python_requires=">=3.9",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Topic :: Utilities",
        ],
        zip_safe=False,
        packages=find_packages(where="src"),
    )
