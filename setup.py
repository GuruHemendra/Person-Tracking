from setuptools import setup,find_packages

HYPHEN_E = "-e."


def get_requirements(file_path : str)->list[str]:    
    requirements = []
    with open(file_path,'r') as file_obj:
        reqs = file_obj.readlines()
        requirements = [ req.strip() for req in reqs]

        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)
    return requirements

setup(
    name="objecttracking",
    description = "A package that will provide trackers like botsort mot , deepsort",
    packages= find_packages(),
)