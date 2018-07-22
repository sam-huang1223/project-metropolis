import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="Project Metropolis",
    version="0.0.1",
    author="Sam Huang",
    author_email="sam.huang@queensu.ca",
#    description="",
    install_requires=['py2neo', 'gspread', 'pandas', 'xlrd', 'flask', 'flask-restful']
#    long_description=long_description,
#    long_description_content_type="text/markdown",
#    url="https://github.com/pypa/example-project",
#    packages=setuptools.find_packages(),
#    classifiers=(
#        "Programming Language :: Python :: 3",
#        "License :: OSI Approved :: MIT License",
#        "Operating System :: OS Independent",
#    ),
)