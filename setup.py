import os
from distutils.core import setup
from setuptools import find_packages


here = os.path.abspath(os.path.dirname(__file__))

VERSION = "0.12"
DESCRIPTION = "Download Manga into chapterwise PDF files"

with open("requirements.txt") as f:
    required_dependencies = f.read().splitlines()


setup(
    name="manga-scraper",
    version=VERSION,
    author="geekyRakshit (Soumik Rakshit)",
    author_email="19soumik.rakshit96@gmail.com",
    description=DESCRIPTION,
    url="https://github.com/soumik12345/Manga-Scraper",
    long_description_content_type="text/markdown",
    long_description=open(os.path.join(here, "README.md")).read(),
    packages=find_packages(),
    install_requires=required_dependencies,
    keywords=["python", "manga", "comic", "scrape"],
    entry_points={
        "console_scripts": [
            "scrapemanga=manga_scraper.__main__:download",
            "installmanga=manga_scraper.__main__:install_mangadl",
        ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Other Audience",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Topic :: Games/Entertainment",
    ],
)
