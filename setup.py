# coding: utf-8

"""
    Nightscout API

    Own your DData with the Nightscout API  # noqa: E501

    OpenAPI spec version: 14.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "nightscout-python-client"
VERSION = "0.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Nightscout API",
    author_email="",
    url="",
    keywords=["Swagger", "Nightscout API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Own your DData with the Nightscout API  # noqa: E501
    """
)
