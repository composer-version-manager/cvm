from setuptools import setup, find_packages

setup(
    name='Composer Version Manager',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cvm=cvm.cli:main',
        ],
    },
    python_requires='>=3'
)