import setuptools

setuptools.setup(
    name="tango-snap7-simulator",
    version="0.1.0",
    author="Sebastian Jennen",
    author_email="sj@imagearts.de",
    description="tango-snap7-simulator device driver",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=['requests'],
    scripts=['Snap7Simulator.py']
)