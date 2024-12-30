from setuptools import setup, find_packages

setup(
    name='package_tracker',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'package-tracker=package_tracker.cli:cli',
        ],
    },
)
