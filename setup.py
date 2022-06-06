from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in print_utils/__init__.py
from print_utils import __version__ as version

setup(
	name="print_utils",
	version=version,
	description="Print Utilities for Frappe Framework",
	author="SpaceCode",
	author_email="p@spacecode.co.th",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
