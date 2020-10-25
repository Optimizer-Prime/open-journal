from setuptools import setup

setup(
    name='open-journal-Optimizer-Prime',
    version='1.0.0',
    install_requires=[
    	'pyqt5',
    	'cryptography'
    ],
    url='https://github.com/Optimizer-Prime/open-journal',
    license='GPL-3.0',
    author='Stuart Clayton',
    author_email='stu3cla@pm.me',
    description='A simple, private, open-source journal.',
    classifiers=["Programming Language :: Python :: 3"],
    python_requires='>=3.6',
    entry_points = {
    'console_scripts': [
        'openjournal=src.openjournal:main']
        }
)
