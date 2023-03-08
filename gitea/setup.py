# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.18.3
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "swagger-client"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
    "aiohttp >= 3.0.0",
    "pydantic",
    "aenum",
]

setup(
    name=NAME,
    version=VERSION,
    description="Gitea API.",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Gitea API."],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type="text/markdown",
    long_description="""\
    This documentation describes the Gitea API.  # noqa: E501
    """,
)
