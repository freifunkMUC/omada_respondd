import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="omada_respondd",
    version="VERSION",
    author="Annika Wickert",
    author_email="aw@awlnx.space",
    description=("A tool to display Omada APs on Freifunk maps."),
    license="GPLv3",
    keywords="Omada Freifunk",
    url="http://packages.python.org/omada_respondd",
    packages=["omada_respondd"],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        "geopy==2.2.0",
        "pyyaml==6.0",
        "dataclasses_json==0.5.6",
    ],
)
