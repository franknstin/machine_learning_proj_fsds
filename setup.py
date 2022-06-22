from setuptools import setup, find_packages
from typing import List


REQUIREMENTS_FILENAME = 'requirements.txt'


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return the list of requirements
    mentioned in the requirements.txt file

    This function is going to return the list which contains name of libraries mentioned
    in the requirements.txt file
    """
    with open(REQUIREMENTS_FILENAME) as requirement_file:
        return requirement_file.readlines().remove('-e .')

setup(
name = "housing-predictor",
version = "0.0.1",
author = "abhishek",
description = "first fsds nov batch machine learning project",
packages = find_packages(),
install_requires = get_requirements_list()
)

