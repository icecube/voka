import pathlib
import pkg_resources
from setuptools import setup

with pathlib.Path('requirements.txt').open() as requirements_txt:
    requirements = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name='voka',
    version='0.9.0',    
    description='Histograms comparisons using unsupervised statistical machine learning.',
    url='https://github.com/icecube/voka',
    author='Alex Olivas',
    author_email='alex.r.olivas@gmail.com',
    license='MIT',
    packages=['voka'],
    install_requires=requirements,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
