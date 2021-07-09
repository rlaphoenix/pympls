from setuptools import setup, find_packages

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="pympls",
    version="0.0.1",
    author="PHOENiX",
    author_email="rlaphoenix@pm.me",
    description="A Python Parser for Blu-ray's MPLS Playlist files",
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/rlaphoenix/pympls",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Multimedia :: Video"
    ],
    python_requires=">=3.6"
)
