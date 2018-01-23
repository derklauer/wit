from setuptools import setup

setup(
    name="dslink-python-witts",
    version="0.1.0",
    description="DSLink Template",
    url="http://github.com/IOT-DSA/template-dslink-python",
    author="Dan Erklauer",
    author_email="derklauer@oceaneering.com",
    license="Apache 2.0",
    install_requires=[
        "dslink == 0.6.16",
        "socket",
        "re"
    ]
)
