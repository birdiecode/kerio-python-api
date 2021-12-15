from setuptools import setup

with open("README.md") as file:
    read_me = file.read()

setup(
    name="kerio",
    version="0.1",
    author="birdiecode",
    author_email="birdiecode@protonmail.com",
    license='GPLv3',
    description="API для взаимодейтвия с продуктами Kerio Technologies.",
    long_description=read_me,
    long_description_content_type="text/markdown",
    url="https://github.com/birdiecode/kerio-python-api",
    packages=['kerio'],
    python_requires='>=3.5'
)
