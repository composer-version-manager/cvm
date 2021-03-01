from setuptools import setup, find_packages
import pathlib


requirements_data = pathlib.Path('.', 'requirements.txt').read_text().split('\n')
readme = pathlib.Path('.', 'README.md').read_text()

setup(
    name='composer version manager',
    packages=find_packages(),
    version='1.0.7',
    license='MIT',
    long_description=readme,
    long_description_content_type="text/markdown",
    url = 'https://github.com/composer-version-manager/cvm',
    entry_points={
        'console_scripts': [
            'cvm=cvm.cli:main',
        ],
    },
    install_requires = requirements_data,
    python_requires='>=3',
)
