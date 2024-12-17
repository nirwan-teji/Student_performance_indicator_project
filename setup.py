from setuptools import find_packages, setup
from typing import List

MINUS_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if MINUS_E_DOT in requirements:
            requirements.remove(MINUS_E_DOT)

    return requirements




setup(
    name='Student Performance Prediction',
    version='0.1',
    author='Anubhav Nirwan',
    author_email='nirwana12anubhav@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt') ## we will create the get_requirements function later

)