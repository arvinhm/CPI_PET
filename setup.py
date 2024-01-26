# setup.py
from setuptools import setup, find_packages

setup(
    name='CPI',
    version='1.0',
    packages=find_packages(),
    package_data={'CPIPackage': ['README.md']},
    entry_points={
        'console_scripts': [
            'CPI=CPIPackage.cpi:main'
        ]
    },
    install_requires=[
        'numpy',
        'pydicom',
        'SimpleITK'
    ]
)
