import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cclogs",
    version="1.0.3",
    author="Peter Tomek",
    author_email="tomek@hunifylabs.com",
    description="Colored console logs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tom4c-hunify/colored-console-log",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)
