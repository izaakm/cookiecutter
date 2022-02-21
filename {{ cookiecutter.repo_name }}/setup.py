#!/usr/bin/env python3

'''
The below is copied from:
https://packaging.python.org/tutorials/packaging-projects/
I used the variables from above to fill in the template below, but in some
cases where I didn't know the correct variable (or if it's set in
cookiecutter), I filled in what I thought made sense (eg, '.github_url').
'''

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version="0.0.1",
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    description='{{ cookiecutter.description }}',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='{{ cookiecutter.github_url }}',
    project_urls={
        "Bug Tracker": "{{ cookiecutter.github_url }}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: {% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %} License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

# END.
