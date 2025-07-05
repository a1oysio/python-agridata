from setuptools import setup, find_packages
import re

with open("agridata/__init__.py", "r", encoding="utf-8") as f:
    content = f.read()
match = re.search(r'__version__\s*=\s*"([^"]+)"', content)
if match:
    version = match.group(1)
else:
    raise RuntimeError("Cannot find version in agridata/__init__.py")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agridata",
    version=version,
    description="Python wrapper for the EC AgriData API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    install_requires=["requests"],
    python_requires=">=3.8",
)
