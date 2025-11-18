from setuptools import setup, find_packages

setup(
    name='quicktrack4115',
    version='0.1.0',
    packages=find_packages(),
    author='Mrunal',
    description='A lightweight Python library for vehicle check-in and check-out',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mrunalshende4115/quicktrack4115',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)