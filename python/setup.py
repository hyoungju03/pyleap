from io import open
import re
import os
import sys

from setuptools import setup, find_packages

install_requires = [
    'numpy',
    'dynamixel_sdk',
]

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(path, filename)
            paths.append((path, [full_path]))
    return paths

setup(name='pyleap',
        packages=find_packages(),
        install_requires=install_requires,
        include_package_data=True,
        zip_safe=False,
)