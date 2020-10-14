from setuptools import setup

setup(
    name="etherscan-python",
    version="1.0.2",
    description="A minimal, yet complete, python API for etherscan.io.",
    url="https://github.com/pcko1/etherscan-python",
    author="Panagiotis-Christos Kotsias",
    author_email="kotsias.pan@gmail.com",
    license="MIT",
    packages=[
        "etherscan",
        "etherscan.enums",
        "etherscan.modules",
        "etherscan.utils",
        "configs",
    ],
    package_data={"configs": ["*"]},
    install_requires=["requests", "coverage"],
    zip_safe=False,
)
