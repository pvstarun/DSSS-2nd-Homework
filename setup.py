from setuptools import setup, find_packages

setup(
    name="dsss_homework_math_quiz",
    version="0.1.0",
    description="A simple math quiz game for DSSS Homework 2.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="pvstarun",
    author_email="pvstarun21@gmail.com",
    url="https://github.com/pvstarun/DSSS-2nd-Homework",
    packages=find_packages(include=["math_quiz", "math_quiz.*"]),
    install_requires=[
        
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)