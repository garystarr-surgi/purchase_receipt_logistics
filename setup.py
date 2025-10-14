# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# The bench utility uses a regex search on this file.
# The 'name' argument in setup() must be easily parsable.

app_name = "purchase_receipt_logistics"
app_version = "0.0.1" # Must match version in app.json

install_requires = [
    # Add any specific Python dependencies here if needed
]

if __name__ == '__main__':
    setup(
        # Use the literal app_name variable here for easy regex parsing by bench
        name=app_name, 
        version=app_version,
        description="Custom logistics logic for Purchase Receipts.",
        author='Your Company Name',
        author_email='you@example.com',
        packages=find_packages(),
        zip_safe=False,
        include_package_data=True,
        install_requires=install_requires,
        license='MIT'
    )
