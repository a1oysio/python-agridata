from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agridata",
    version="0.1.0",
    description="Python wrapper for the EC AgriData API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    install_requires=["requests"],
    python_requires=">=3.8",
)
