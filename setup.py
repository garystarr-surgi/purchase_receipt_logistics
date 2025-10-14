from setuptools import setup, find_packages

app_name = "purchase_receipt_logistics"

install_requires = []

if __name__ == "__main__":
    setup(
        name=app_name,            # ✅ use variable
        version="0.0.1",          # ✅ literal string
        description="Custom logistics logic for Purchase Receipts.",
        author="SurgiShop",
        author_email="gary.starr@surgishop.com",
        packages=find_packages(),
        include_package_data=True,
        install_requires=install_requires,
        zip_safe=False,
        license="MIT",
        long_description="Custom Frappe app to enhance Purchase Receipt handling with logistics features.",
        classifiers=[
            "Framework :: Frappe",
            "Programming Language :: Python :: 3"
        ]
    )
