import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup

setup(
    name='micropython-tm1637',
    py_modules=['tm1637'],
    version='1.3.0',
    description='MicroPython library for TM1637 LED driver.',
    long_description='This library lets you operate quad 7-segment LED display modules based on the TM1637 LED driver.',
    keywords='tm1637 seven segment led micropython',
    url='https://github.com/mcauser/micropython-tm1637',
    author='Mike Causer',
    author_email='mcauser@gmail.com',
    maintainer='Mike Causer',
    maintainer_email='mcauser@gmail.com',
    license='MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'License :: OSI Approved :: MIT License',
    ],
)