from setuptools import setup, find_packages

setup(
    name="Breakout",
    version="1.0",
    author="Gabriel Knudtson",
    description="A simple Breakout game utilizing pygame and Object Oriented Programming (OOP) principles.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gknudtson/Breakout.git",  # GitHub repo
    packages=find_packages(),  # Automatically find all packages
    python_requires='>=3.10',
    install_requires=[
        'pygame'
    ]
)
