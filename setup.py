from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
    return requirements    






setup(
name='mlproject'
,version='0.0.1'
,author="debabrata das"
,author_email="debabratadas2225@gmail.com"
,packages=find_packages()
,install_requires=get_requirements('requirement.txt')
)    