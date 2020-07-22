import sys

from setuptools import setup

# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='raspberrypi-tm1637',
    py_modules=['tm1637'],
    version='1.3.2',
    description='Raspberry Pi Python port from MicroPython library for TM1637 LED driver.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='tm1637 raspberry pi seven segment led python',
    url='https://github.com/depklyon/raspberrypi-tm1637',
    author='Mike Causer',
    author_email='mcauser@gmail.com',
    maintainer='Patrick Palma',
    maintainer_email='patrick.depalma@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3',
    install_requires=['wiringpi']
)
