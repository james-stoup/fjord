import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="fjord",
    version="1.0.0",
    description=("A better way to use NordVPN from the terminal"),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/james-stoup/fjord",
    author="James Stoup",
    author_email="james.r.stoup@gmail.com",
    keywords="NordVPN Nord VPN",
    license="GNU General Public License v3.0",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=["Click", "MonthDelta", "GitPython"],
    entry_points={"console_scripts": ["fjord=src.main:cli"]},
)
