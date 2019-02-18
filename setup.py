from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='AWS-Invoke',
    version='0.0.2',
    author='PentairIoT',
    author_email='pentairiot@gmail.com',
    description='Python library for Invoking a targeted AWS Lambda function based on the provied event',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pentairiot/Invoke',
    packages=["Invoke"],
    install_requires=["boto3"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
