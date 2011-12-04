from setuptools import setup, find_packages
import os

setup(name='noneurl',
    version='0.0.1',
    description="Custom django URL tag that strip out empty or null kwargs",
    long_description="",
    keywords='',
    author='Xavier Grangier',
    author_email='grangier@gmail.com',
    url='',
    license='GPL',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django',
    ]
)
