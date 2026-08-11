from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    with open(file_path, encoding="utf-8-sig") as file_obj:
        requirements = [
            req.strip()
            for req in file_obj.readlines()
            if req.strip()
        ]

    # Remove editable install
    requirements = [
        req for req in requirements
        if req != HYPHEN_E_DOT
    ]

    return requirements


setup(
    name='mlProject',
    version='0.0.1',
    author='Deepak',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)