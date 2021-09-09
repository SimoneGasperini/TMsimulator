from setuptools import setup
from setuptools import find_packages


setup(

    name='TMsimulator',
    version='0.0.1',

    author='SimoneGasperini',
    author_email='simone.gasperini2@studio.unibo.it',

    description='Turing Machine simulator written in Python',
    url='https://github.com/SimoneGasperini/TMsimulator.git',

    packages=find_packages(),
    python_requires='>=3.8',

)
