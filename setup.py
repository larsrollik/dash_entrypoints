from os import path

from setuptools import find_packages
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md")) as f:
    long_description = f.read()

with open(path.join(this_directory, "LICENSE")) as f:
    license_text = f.read()


setup(
    name="dash_entrypoints",
    version="0.2.3",
    description="Dash entrypoints: Wrapper for dash/dash-labs multi-page app and specific layout elements.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "dash",
        "dash_bootstrap_components",
        "dash_labs==1.0.2",  # for multi-page feature at least version 1.0.2
        "rich",
    ],
    extras_require={
        "dev": [
            "black",
            "pytest-cov",
            "pytest",
            "gitpython",
            "coverage>=5.0.3",
            "bump2version",
            "pre-commit",
            "flake8",
        ]
    },
    python_requires=">=3.6",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ifentry = dash_entrypoints.__init__:run_cli",
        ],
    },
    author="Lars B. Rollik",
    author_email="L.B.ROLLIK@protonmail.com",
    license=license_text,
    include_package_data=True,  # + zip_safe=False + MANIFEST.in recursive include package *.glob
    zip_safe=False,
)
