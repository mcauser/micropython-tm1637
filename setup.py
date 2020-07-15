import sys

from setuptools import setup

# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)

setup(
    name='raspberrypi-python-tm1637',
    py_modules=['tm1637'],
    version='1.3.0',
    description='Raspberry Pi Python port from MicroPython library for TM1637 LED driver.',
    long_description='This library lets you operate quad 7-segment LED display modules based on the TM1637 LED driver '
                     'with Raspberry PI.',
    keywords='tm1637 raspberry pi seven segment led python',
    url='https://github.com/depklyon/raspberrypi-python-tm1637',
    author='Mike Causer',
    author_email='mcauser@gmail.com',
    maintainer='Patrick Palma',
    maintainer_email='patrick.depalma@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
