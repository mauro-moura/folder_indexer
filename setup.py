from setuptools import setup

setup(
    name='pindexer',
    version='0.1',
    packages=['src'],
    entry_points={
        'console_scripts': [
            'pindexer = src.main:main'
        ]
    },
)
