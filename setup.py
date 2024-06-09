from setuptools import find_packages,setup
from typing import List

HYPEN_e_dot ='-e .'

def get_requirements(file_path:str)-> List[str]:          #get_requirement will return list for input file path as string
    requirements=[]
    with open(file_path) as file_obj:             #file_obj is alias for file name
        requirements= file_obj.readlines()      # to read each line but each line will have \n with itself
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_e_dot in requirements:
            requirements.remove(HYPEN_e_dot)
        
        return requirements


setup(                                               # package info ,we can also change it
    name='DiamondPricePrediction',
    version='0.0.1',
    author='niket',
    author_email='niketanand420@gmail.com',
    install_requires=get_requirements('requirement.txt'),        # u can also directly wrtie the packages required here or use the function to read requirements.txt
    packages=find_packages()
)