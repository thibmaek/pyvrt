import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyvrt",
    version="1.6.0",
    author="thibmaek",
    author_email="thibault.maekelbergh@icloud.com",
    description="Python library to interact with VRT public APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thibmaek/pyvrt",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
