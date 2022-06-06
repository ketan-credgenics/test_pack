from setuptools import setup, find_packages
setup(
    name='cg_database',
    packages=find_packages(),
    description='DB Library for Credgenics',
    version='0.2.2',
    url='',
    author='Mehul Mittal',
    author_email='mehul.mittal@credgenics.com',
    install_requires = [
        "Quart==0.17.0",
        "asyncpg==0.21.0"
    ]
)
