import setuptools
from importlib.machinery import SourceFileLoader

version = SourceFileLoader(
    "projectaile.version", "projectaile/version.py").load_module()

with open("requirements.txt", "r") as fp:
    required = fp.read().splitlines()

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="projectaile",
    version=version.__version__,
    author="Anubhav Tiwari",
    author_email="abt.exp@gmail.com",
    description="A framework agnostic architecture and utility library \
                for all machine learning and deep learning projects \
                providing an abstract and easy to use but still very configurable API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abtExp/projectaile",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    project_urls={
        "Source": "https://github.com/abtExp/projectaile",
        "Tracker": "https://github.com/abtExp/projectaile/issues",
    },
    python_requires=">=3.6",
    install_requires=required,
    extras_require={
        "testing": [
            "pytest",
            "coverage",
            "pytest-mock",
            "pylint",
            "mypy"
        ]
    },
    entry_points={
        "console_scripts": [
            "generate = projectaile.utils:generate_project",
        ]
    }
)
