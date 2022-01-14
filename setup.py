from setuptools import setup

setup(
    name='voka',
    version='0.9.0',    
    description='Histograms comparisons using unsupervised statistical machine learning.',
    url='https://github.com/icecube/voka',
    author='Alex Olivas',
    author_email='alex.r.olivas@gmail.com',
    license='MIT',
    packages=['voka'],
    install_requires=[
        'cycler==0.10.0',
        'kiwisolver==1.1.0',
        'matplotlib==3.2.0',
        'numpy==1.18.1',
        'pyparsing==2.4.6',
        'python-dateutil==2.8.1',
        'six==1.14.0'
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
