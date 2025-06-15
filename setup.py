from setuptools import setup, find_packages

setup(
    name="agridata",
    version="0.1.0",
    description="Python wrapper for the EC AgriData API",
    packages=[
        "agridata",
        "agridata.endpoints",
        "agridata.queries",
        "agridata.models",
        "agridata.exceptions",
    ],
    install_requires=["requests", "httpx"],
)
