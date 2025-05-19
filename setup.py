from setuptools import setup, find_packages
from typing import List

HYPEN_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    # This function is used to return a list of requirements
    
    with open(file_path) as file_obj:
        requirements = []
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Pranit Gore',
    author_email = 'pranitgore0605@gmail.com',
    packages = find_packages(),
    install_requirements = get_requirements('requirements.txt'),
)