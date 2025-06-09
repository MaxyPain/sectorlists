from setuptools import setup, find_packages

setup(
    name='nseutility',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
        'beautifulsoup4'
    ],
    author='Max',
    author_email='maxpain@example.com',
    description='A Python utility to fetch live data from NSE India',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MaxPain/nseutility',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
