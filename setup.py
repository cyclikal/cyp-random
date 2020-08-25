import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
shrt = "Example Cyckei Plugin Package, Generates Random Numbers"

setuptools.setup(
    name="cyp-randomizer",
    version="1.0",
    author="Gabriel Ewig",
    author_email="gabriel@cyclikal.com",
    description=shrt,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyclikal/cyp-random",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
    ],
    python_requires='>=3.6',
)
