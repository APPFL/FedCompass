import setuptools

# Build Author list
authors = {
    "Zilinghan Li": "zilinghan.li@anl.gov",
}
AUTHOR = ""
for i, (k, v) in enumerate(authors.items()):
    if i > 0:
        AUTHOR += ", "
    AUTHOR += f"{k} <{v}>"

setuptools.setup(
    name="appfl",
    version="0.1.0",
    author=AUTHOR,
    description="Source code for FedCompass",
    url="https://github.com/APPFL/FedCompass",
    project_urls={
        "Bug Tracker": "https://github.com/APPFL/FedCompass/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "torch",
        "grpcio",
        "grpcio-tools",
        "omegaconf",
        "matplotlib",
        "torchvision",
        "globus-sdk",
        "mpi4py",
        "zfpy",
        "blosc",
        "zstd",
        "scipy",
        "lz4",
        "python-xz",
    ],
    entry_points={
        "console_scripts": [
            "appfl-auth=appfl.login_manager.globus.cli:auth",
            "appfl-install-compressor=appfl.compressor.install:install_compressor",
        ],
    },
)
