import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

import codecs
import os.path

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        return line
    else:
        raise RuntimeError("Unable to find version string.")

print("X", get_version("VERSION"))

setuptools.setup(
    name="testing_gha_dummy", # Replace with your own username
    version = get_version("VERSION"),
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://test.pypi.org/project/testing-gha-dummy/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)