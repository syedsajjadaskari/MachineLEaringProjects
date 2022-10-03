from setuptools import setup
from typing import List

REQUIRMENTS_FILE_NAME = "requirments.txt"

def get_requirmnets_details()->List(str):
    """
    this function is going to return the function in requirments
    
    return this function is going to retunt list of library whic contains
    library in requirments.txt file """
    with open(REQUIRMENTS_FILE_NAME) as requirment_file:
        return requirment_file.readlines()
    

NAME = "house-predictor",
VERSIONS="0.0.1",
AUTHOR = "SYED SAJJAD ASKARI", 
DESCRIPTION = "this is the first machine learing projects"
PACKAGES=["housing"]

setup(
    name = NAME,
    version=VERSIONS,
    author = AUTHOR,
    description=DESCRIPTION,
    package = PACKAGES,
    install_requirments = get_requirmnets_details()

)

