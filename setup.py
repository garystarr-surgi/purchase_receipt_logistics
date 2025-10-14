# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# Load app metadata from app.json
import json
with open('app.json') as f:
    app_metadata = json.load(f)

# Define the app variables based on app.json
app_name = app_metadata['name']
app_title = app_metadata['title']
app_description = app_metadata['description']
app_version = app_metadata['version']
app_license = app_metadata['license']

# List of all Python packages required for the app
# (Frappe apps typically rely on 'frappe' itself)
install_requires = [
    # Add any specific Python dependencies here if needed
]

if __name__ == '__main__':
    setup(
        name=app_name,
        version=app_version,
        description=app_description,
        author='SurgiShop',  # Use publisher from app.json
        author_email='gary.starr@surgishop.com', # Use email from app.json
        packages=find_packages(),
        zip_safe=False,
        include_package_data=True,
        install_requires=install_requires,
        dependency_links=[],
        entry_points={
            'console_scripts': [
                # Add command line entry points if necessary
            ]
        },
        license=app_license
    )

