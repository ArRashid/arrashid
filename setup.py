import os
from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)

# Function to read the requirements from a file
def get_requirements():
    with open(os.path.join(base_dir, 'requirements.txt'), 'r') as file:
        requirements = file.readlines()
    return [line.strip() for line in requirements if not line.strip().startswith('#')]


with open(os.path.join(base_dir, "README.md"), encoding="utf8") as f:
    readme = f.read()
    

with open(os.path.join(base_dir, "CHANGES.md"), encoding="utf8") as f:
    changes = f.read()


setup(
    name="arrashid",
    version="0.1.0",
    description="This module streamlines and accelerates coding and automation processes across various aspects of your program.",
    long_description="{}\n\n{}".format(readme, changes),
    long_description_content_type = "text/x-rst",
    author='Abdur Rashid Mondal',
    author_email="ar.rashid.mondal@gmail.com",
    url="https://in.linkedin.com/in/abdur-rashid-mondal",
    license="MIT",
    packages = ['arrashid',  'arrashid.extras'],
    install_requires=get_requirements(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
      'Development Status :: 1 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Topic :: Genaral',
    ]
    )

