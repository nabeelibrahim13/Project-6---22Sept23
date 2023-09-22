from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]        

    return requirements
setup(
name='Project 6 - 22Sept23',
version='0.0.1',
author='Muhammad Nabeel',
author_email='mnibrahim@cloud.neduet.edu.pk',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)