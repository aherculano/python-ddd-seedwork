import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ddd-seedwork",
    version="0.0.1",
    author="Alexandre Rodrigues",
    author_email="aherculano0109@gmail.com",
    description="A small ddd_seedwork with support for flask",
    licence='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aherculano/python-ddd-seedwork",
    packages=setuptools.find_packages(include=['ddd_seedwork*']),
    install_requires=[
        "flask>=1.1.2"
    ],
    python_requires='>=3.6',
)
