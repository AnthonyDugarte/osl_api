from setuptools import find_packages, setup


setup(
    name='osl_api',
    version='0.0.1',
    packages=find_packages(),
    author="Anthony Dugarte",
    author_email="toonny1998@gmai.com",
    description="Simple Python OSL Exchange API client which handles authorization for you and exposes a requests-like interface",
    url="https://github.com/AnthonyDugarte/osl_api",
    python_requires='>=3.5',
)
