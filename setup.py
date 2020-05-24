import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dockerfile-api",
    version="0.0.1",
    author="Stewart Platt",
    author_email="shteou@gmail.com",
    description="An API for constructing Dockerfiles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shteou/dockerfile-api",
    packages=["dockerfile_api"],
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

