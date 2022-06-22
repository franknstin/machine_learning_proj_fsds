from setuptools import setup
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
        return requirement_file.readline()

setup(
name = "housing-predictor",
version = "0.0.1",
author = "abhishek",
description = "first fsds nov batch machine learning project",
packages = ["housing"],
install_requires = get_requirements_list()
)


if __name__ == "__main__":
    print(get_requirements_list())