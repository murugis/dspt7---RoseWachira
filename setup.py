import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dspt7---RoseWachira", # Replace with your own username
    version="0.0.3",
    author="Rose Wachira",
    author_email="waridicook@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/murugis/dspt7---RoseWachira",
    packages=['my_lambdata'],# added init on test not a package so we specify 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)