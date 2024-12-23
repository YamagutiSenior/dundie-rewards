from setuptools import setup, find_packages
import os

def read(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

def read_requirements(*paths):
    return read(*paths).strip().split('\n')

setup (
    name="dundie",
    version="0.1.0",
    description="Reward Point System for Dunder Mifflin",
    author="Tiago Yamaguti",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dundie = dundie.__main__:main'
        ]
    }
)

install_requires=[],

extras_require={
        'test': [
            'pytest'
        ],  # Included for testing purposes only
        'dev': [
            'ipython', 
            'ipd', 
            'mypy'] 
        }


