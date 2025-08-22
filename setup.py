# setuptools is a package that provides tools for packaging python package
from setuptools import find_packages, setup
from typing import List
# update 
def get_requirements(file_path : str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


setup(
    name = "Fault detection",
    version = '0.0.1',
    author = 'ridham',
    author_email = 'inaniridham@gmail.com',
    install_requires = get_requirements('requirements.txt'), # dependencies
    packages = find_packages()
)