from setuptools import setup

setup(
    name="etherscan-python",
    version="1.0.0",
    description="A minimal, yet complete, python API for etherscan.io.",
    url="https://github.com/pcko1/etherscan-python",
    author="Panagiotis-Christos Kotsias",
    author_email="kotsias.pan@gmail.com",
    license="MIT",
    packages=["etherscan"],
    install_requires=["requests", "coverage"],
    zip_safe=False,
)
