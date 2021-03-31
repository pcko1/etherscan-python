from setuptools import setup

setup(
    name="etherscan-python",
    version="2.1.0",
    description="A minimal, yet complete, python API for etherscan.io.",
    url="https://github.com/pcko1/etherscan-python",
    author="Panagiotis-Christos Kotsias",
    author_email="kotsias.pan@gmail.com",
    license="MIT",
    packages=[
        "etherscan",
        "etherscan.configs",
        "etherscan.enums",
        "etherscan.modules",
        "etherscan.utils",
    ],
    install_requires=["requests"],
    include_package_data=True,
    zip_safe=False,
)
