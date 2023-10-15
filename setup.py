from setuptools import setup

setup(
    name='lab3',
    version='0.1',
    description='lab № 2',
    author='Maksina Elizaveta',
    packages=['lab3'],
    scripts = ['run.py'],
    install_requires=[
        'numpy',
        'requests',
        'matplotlib',
        'jsons',
        'datetime'
    ],
)