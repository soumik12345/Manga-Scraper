import os
import subprocess
from distutils.core import setup
from setuptools import find_packages
from setuptools.command.install import install


here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.2'
DESCRIPTION = 'Download Manga into chapterwise PDF files'

with open('requirements.txt') as f:
    required_dependencies = f.read().splitlines()


class CustomInstallCommand(install):
    """Custom install setup to help run shell commands (outside shell) before installation"""
    
    def run(self):
        subprocess.run([
            "curl",
            "--compressed",
            "-s",
            "https://raw.githubusercontent.com/Akianonymus/mangadl-bash/master/release/install",
            "|",
            "bash",
            "-s"
        ])
        install.run(self)

# Setting up
setup(
    name="manga-scraper",
    version=VERSION,
    author="geekyRakshit (Soumik Rakshit)",
    author_email="19soumik.rakshit96@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open(os.path.join(here, "README.md")).read(),
    packages=find_packages(),
    install_requires=required_dependencies,
    keywords=['python', 'manga', 'comic', 'scrape'],
    cmdclass={"install": CustomInstallCommand},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Other Audience",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Topic :: Games/Entertainment"
    ]
)
